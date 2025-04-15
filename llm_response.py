import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer

from sleeper import llm_ask  # Importing the simulated LLM function

class LLMThread(QThread):
    response_ready = pyqtSignal(str)

    async def get_response(self, question):
        response = await llm_ask(question)
        self.response_ready.emit(response)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.get_response(self.question))

class ChatbotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chatbot")
        self.setGeometry(100, 100, 400, 600)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setAlignment(Qt.AlignLeft)

        self.input_field = QLineEdit()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_question)

        self.thinking_label = QLabel("")
        self.thinking_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.thinking_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.llm_thread = None

    def send_question(self):
        question = self.input_field.text().strip()
        if not question:
            return

        # Display the user message
        self.display_message(f"<b>User:</b><div style='background-color: black; color: white; border-radius: 5px; padding: 5px; margin: 5px;'>{question}</div>", "user")

        self.input_field.clear()
        self.start_thinking_indicator()

        self.llm_thread = LLMThread()
        self.llm_thread.question = question
        self.llm_thread.response_ready.connect(self.display_response)
        self.llm_thread.start()

    def display_message(self, message, sender):
        if sender == "user":
            # User message is displayed with specific styling
            self.chat_area.append(message)
        else:
            # Bot messdisplage is displayed with specific styling
            styled_message = f"<b>Bot:</b><div style='background-color: lightblue; color: white; border-radius: 5px; padding: 5px; margin: 5px;'>{message}</div>"
            self.chat_area.append(styled_message)
        
        # Scroll to the bottom of the chat area
        self.chat_area.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())

    def display_response(self, response):
        self.stop_thinking_indicator()
        self.display_message(response, "bot")

    def start_thinking_indicator(self):
        self.thinking_label.setText("Thinking.")
        self.update_thinking_indicator()

    def update_thinking_indicator(self):
        if self.thinking_label.text() == "Thinking...":
            self.thinking_label.setText("Thinking.")
        elif self.thinking_label.text() == "Thinking.":
            self.thinking_label.setText("Thinking..")
        elif self.thinking_label.text() == "Thinking..":
            self.thinking_label.setText("Thinking...")
        QTimer.singleShot(500, self.update_thinking_indicator)

    def stop_thinking_indicator(self):
        self.thinking_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = ChatbotApp()
    chatbot.show()
    sys.exit(app.exec_())
