import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt
#from sleeper import llm
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat")
        self.setGeometry(100, 100, 400, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.chat_area = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_area)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.chat_area)

        self.input = QLineEdit()
        self.layout.addWidget(self.input)

        self.send = QPushButton("Send")
        self.send.clicked.connect(self.message)
        self.layout.addWidget(self.send)

    def message(self):
        text = self.input.text().strip()
        if text:
            mcon = QWidget()
            mlay = QHBoxLayout(mcon)

            uml = QLabel(text)
            uml.setStyleSheet("background-color: blue; color: white; padding : 5px; border-radius: 5px;")
            uml.setAlignment(Qt.AlignLeft)
            uml.setWordWrap(True)
            mlay.addWidget(uml, alignment=Qt.AlignLeft)
            
            rt = f"Here's what you said: {text}"
            bml = QLabel(rt)
            bml.setStyleSheet("background-color: black; color: white; padding : 5px; border-radius: 5px;")
            bml.setAlignment(Qt.AlignRight)
            bml.setWordWrap(True)
            # bml.setMinimumWidth(200)
            # bml.setMinimumHeight(1000)
            mlay.addWidget(bml, alignment=Qt.AlignRight)

            self.chat_layout.addWidget(mcon)
            self.input.clear()
            self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())