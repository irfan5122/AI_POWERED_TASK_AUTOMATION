import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QFont, QIcon, QColor
from PyQt6.QtCore import Qt


class ModernAdvancedUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window Settings
        self.setWindowTitle("AI Task Automation - Modern UI")
        self.setGeometry(100, 100, 850, 550)
        self.setStyleSheet("background-color: #121212;")  # Dark Theme
        
        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 255, 255, 150))  # Cyan glow effect

        # Header Label
        self.header_label = QLabel("AI Task Automation")
        self.header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.header_label.setStyleSheet("color: white; margin-bottom: 20px;")
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Voice Mode Button - 3D Effect
        self.voice_button = QPushButton("🎙 Voice Mode")
        self.voice_button.setFixedSize(220, 220)
        self.voice_button.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.voice_button.setGraphicsEffect(shadow)
        self.voice_button.setStyleSheet("""
            QPushButton {
                background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.8, 
                                            fx:0.5, fy:0.5, stop:0 #ff0000, stop:1 #8b0000);
                color: white;
                border-radius: 110px;
                border: 5px solid #ff4444;
                font-size: 20px;
            }
            QPushButton:hover {
                border-color: cyan;
                background: #ff6666;
            }
            QPushButton:pressed {
                background: #ff2222;
            }
        """)

        # Task Entry Box with Neon Effect
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter the task here...")
        self.task_entry.setFixedSize(520, 55)
        self.task_entry.setFont(QFont("Arial", 14))
        self.task_entry.setStyleSheet("""
            QLineEdit {
                background-color: rgba(30, 30, 30, 200);
                color: cyan;
                border: 2px solid #ff4444;
                border-radius: 25px;
                padding-left: 15px;
                selection-background-color: rgba(0, 255, 255, 100);
            }
            QLineEdit:focus {
                border-color: cyan;
                background-color: rgba(40, 40, 40, 255);
            }
        """)
        self.task_entry.returnPressed.connect(self.on_send)  # Bind Enter key

        # Send Button with Hover Animation
        self.send_button = QPushButton("➤")
        self.send_button.setFixedSize(65, 55)
        self.send_button.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(80, 80, 80, 200);
                color: cyan;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: cyan;
                color: black;
                font-size: 24px;
            }
            QPushButton:pressed {
                background-color: #00bcd4;
            }
        """)
        self.send_button.clicked.connect(self.on_send)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.header_label)

        # Centered Voice Button
        layout.addWidget(self.voice_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Task Entry Layout
        entry_layout = QHBoxLayout()
        entry_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        entry_layout.addWidget(self.task_entry)
        entry_layout.addWidget(self.send_button)

        layout.addSpacing(20)
        layout.addLayout(entry_layout)

        self.setLayout(layout)

    def on_send(self):
        message = self.task_entry.text()
        if message.strip():
            print(f"📌 Task Received: {message}")
            import text_analyzer

            actions, objects = text_analyzer.process_command(message)


        else:
            print("⚠ No task entered!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernAdvancedUI()
    window.show()
    sys.exit(app.exec())