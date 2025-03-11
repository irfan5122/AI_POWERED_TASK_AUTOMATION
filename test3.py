import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QFont, QColor, QIcon
from PyQt6.QtCore import Qt

class ModernUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window Settings
        self.setWindowTitle("AI Task Automation")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: black;")

        # Voice Mode Button (Circular Style)
        self.voice_button = QPushButton("VOICE MODE")
        self.voice_button.setFixedSize(200, 200)
        self.voice_button.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.voice_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: black;
                border-radius: 100px;
                font-size: 24px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        # Task Entry Field
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter the task here")
        self.task_entry.setFixedSize(500, 50)
        self.task_entry.setFont(QFont("Arial", 14))
        self.task_entry.setStyleSheet("""
            QLineEdit {
                background-color: black;
                color: cyan;
                border: 2px solid red;
                border-radius: 25px;
                padding: 10px;
            }
            QLineEdit:focus {
                border-color: cyan;
            }
        """)
        self.task_entry.returnPressed.connect(self.on_send)  # Bind Enter key

        # Send Button (Styled)
        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(60, 50)
        self.send_button.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: grey;
                color: cyan;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkgrey;
            }
        """)
        self.send_button.clicked.connect(self.on_send)

        # Layouts
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.voice_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Task Entry Layout (Horizontal)
        entry_layout = QHBoxLayout()
        entry_layout.addWidget(self.task_entry)
        entry_layout.addWidget(self.send_button)

        layout.addLayout(entry_layout)

        self.setLayout(layout)

    def on_send(self):
        message = self.task_entry.text()
        if message.strip():
            print("Task:", message)
        else:
            print("No message entered.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernUI()
    window.show()
    sys.exit(app.exec())