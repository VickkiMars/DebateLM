import sys
import asyncio
import requests
import random
from PyQt5 import uic
from qasync import QEventLoop, asyncSlot
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from sleeper import llm_ask

class LLMThread(QThread):
    response_ready = pyqtSignal(list)

    async def get_response(self, question):
        response = await llm_ask(question)
        self.response_ready.emit(response)

    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.get_response(self.question))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        uic.loadUi("debate.ui", self)

        self.input_field = self.findChild(QLineEdit, "input")
        self.send_button = self.findChild(QPushButton, "send")
        self.connecting = self.thinking_label = self.findChild(QLabel, "connecting")
        self.large = self.findChild(QLabel, "biglabel")
        self.widdy = self.findChild(QWidget, "widget")
        self.topic = self.findChild(QLabel, "topic")

        self.vl = QVBoxLayout(self.widdy)
        self.sa = QScrollArea()
        self.sa.setWidgetResizable(True)
        #self.vl.addWidget(self.sa)

        self.label_container = QWidget()
        self.vl2 = QVBoxLayout(self.label_container)
        self.sa.setWidget(self.label_container)

        self.vl.addWidget(self.sa)


        #self.chat_area = self.widdy
        #self.clay = QVBoxLayout(self.chat_area)
        self.vl.setAlignment(Qt.AlignTop)
        #self.sa.setWidget(self.widdy)
        self.large.raise_()

        self.send_button.clicked.connect(self.handle_send)

        self.llm_thread= None
        self.boolish = False

    def check_connection(self):
        try:
            requests.get("https://www.google.com", timeout=3)
            self.connecting.setText("Connected 🟢")
        except requests.ConnectionError:
            self.connecting.setText("No Connection 🔴")

    def handle_send(self):
        text = self.input_field.text().strip()
        self.topic.setText(text.title())
        #self.display_message(text, "user")
        self.input_field.clear()
        self.start_thinking_indicator()

        self.llm_thread = LLMThread()
        self.llm_thread.question = text
        self.llm_thread.response_ready.connect(self.display_response)
        self.llm_thread.start()

    def display_message(self, message, sender):
        if "too" in message:
            new_label = self.create_right_aligned_label("The model couldn't reply in 60 seconds, please try again", "expert1")
            self.vl2.addWidget(new_label)
            self.sa.verticalScrollBar().setValue(self.sa.verticalScrollBar().maximum())
        else:
            message = message.split("\n\n")
            speaker1 = []
            speaker2 = []
            last = 0
            for i in message:
                if i.startswith("Expert 1"):
                    speaker1.append(i)
                    last  = 1
                elif i.startswith("Expert 2"):
                    speaker2.append(i)
                    last = 2
                else:
                    if last == 1:
                        speaker1[-1] += i
                    else:
                        speaker2[-1] += i

            self.large.setText("")
            for i, j in zip(speaker1, speaker2):
                new_label = self.create_right_aligned_label(i, "expert1")
                self.vl2.addWidget(new_label)
                self.sa.verticalScrollBar().setValue(self.sa.verticalScrollBar().maximum())
                time.sleep(random.uniform(0.1, 0.5))
                new_label = self.create_right_aligned_label(j, "expert2")
                self.vl2.addWidget(new_label)
                self.sa.verticalScrollBar().setValue(self.sa.verticalScrollBar().maximum())
                time.sleep(random.uniform(0.1, 0.5))
            #self.widdy.verticalScrollBar().setValue(self.chat_area.verticalScrollBar().maximum())

    def create_right_aligned_label(self, text, sender):
        disc_colo = "rgb(51, 51, 153)"
        # if sender == "expert1":
        #     label_widget = QWidget()
        #     layout = QVBoxLayout(label_widget)
        #     label = QLabel(text)
        #     layout.addWidget(label, alignment=Qt.AlignRight)
        #     label_widget.setStyleSheet("font: 10pt 'Montserrat'; background: white; color: rgb(51, 51, 153); border-radius: 15px; padding: 5px;")

        if sender == "expert1":
            label_widget = QWidget()
            layout = QVBoxLayout(label_widget)
            label = QLabel(text)
            label.setWordWrap(True)
            layout.addWidget(label, alignment=Qt.AlignRight)
            label_widget.setStyleSheet(f"font: 10pt 'Montserrat';background: {disc_colo}; color: rgb(236, 236, 249); border-radius: 15px; padding: 5px;")
        else:
            label_widget = QWidget()
            layout = QVBoxLayout(label_widget)
            label = QLabel(text)
            label.setWordWrap(True)
            layout.addWidget(label, alignment=Qt.AlignRight)
            label_widget.setStyleSheet(f"font: 10pt 'Montserrat';background: black; color: rgb(236, 236, 249); border-radius: 15px; padding: 5px;")
            time.sleep(random.uniform(0.1, 0.5))


        return label_widget

    def display_response(self, response):
        self.stop_thinking_indicator()
        self.display_message(message=response, sender="bot")

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
        self.check_connection()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot = MainWindow()
    chatbot.show()
    sys.exit(app.exec_())
    import gc
    gc.collect()
