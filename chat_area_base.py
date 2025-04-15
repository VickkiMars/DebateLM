from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea
from PyQt5.QtCore import Qt
class LabelApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dynamic Label Example")
        self.resize(300, 200)

        # Main layout for the main widget
        self.main_layout = QVBoxLayout(self)

        # Button to add new labels
        self.add_label_button = QPushButton("Add Label")
        self.add_label_button.clicked.connect(self.add_new_label)

        # Layout for the labels
        self.label_layout = QVBoxLayout()
        self.sa = QScrollArea()
        

        # Adding button and label layout to the main layout
        self.main_layout.addLayout(self.label_layout)
        self.main_layout.addWidget(self.add_label_button)

    def add_new_label(self):
        # Create a new label with dynamic text
        label_text = f"This is label {self.label_layout.count() + 1}"
        new_label = self.create_right_aligned_label(label_text)
        # Add the new label to the label layout
        self.label_layout.addWidget(new_label)

    def create_right_aligned_label(self, text):
        # Create a QWidget to hold the QLabel
        label_widget = QWidget()
        # Create a QVBoxLayout for the widget
        layout = QVBoxLayout(label_widget)
        
        # Create the QLabel
        label = QLabel(text)
        
        # Add the label to the layout and set its alignment to right
        layout.addWidget(label, alignment=Qt.AlignRight)
        
        # Optional: Set the style for the QLabel
        label_widget.setStyleSheet("background-color: lightblue; padding: 5px; border-radius: 5px;")
        
        return label_widget

if __name__ == "__main__":
    app = QApplication([])

    # Create and show the label application
    label_app = LabelApp()
    label_app.show()

    app.exec_()
