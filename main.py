import sys
import speech_recognition as sr
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QFont, QIcon, QColor
from PyQt6.QtCore import Qt


class ModernAdvancedUI(QWidget):
    def __init__(self):
        super().__init__()
        self.is_listening = False  # Track listening state
        self.recognizer = sr.Recognizer()  # Speech recognizer instance
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
        self.task_entry.returnPressed.connect(self.on_send)

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
        self.voice_button.clicked.connect(self.toggle_voice_mode)

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

    def toggle_voice_mode(self):
        if not self.is_listening:
            # Start listening
            self.is_listening = True
            self.voice_button.setStyleSheet("""
                QPushButton {
                    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.8, 
                                                fx:0.5, fy:0.5, stop:0 #00aaaa, stop:1 #008b8b);
                    color: white;
                    border-radius: 110px;
                    border: 5px solid cyan;
                    font-size: 20px;
                }
            """)
            self.voice_button.setText("🎙 Listening...")
            
            # Start voice recognition in a separate thread to avoid UI freeze
            import threading
            threading.Thread(target=self.listen_and_convert, daemon=True).start()
        else:
            # Stop listening
            self.is_listening = False
            self.voice_button.setStyleSheet("""
                QPushButton {
                    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.8, 
                                                fx:0.5, fy:0.5, stop:0 #ff0000, stop:1 #8b0000);
                    color: white;
                    border-radius: 110px;
                    border: 5px solid #ff4444;
                    font-size: 20px;
                }
            """)
            self.voice_button.setText("🎙 Voice Mode")

    def listen_and_convert(self):
        try:
            with sr.Microphone() as source:
                print("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source)
                print("Ready to listen...")
                while self.is_listening:
                    try:
                        print("Listening...")
                        audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
                        print("Processing...")
                        text = self.recognizer.recognize_google(audio)
                        print(f"Recognized: {text}")
                        self.task_entry.setText(text)  # Update the text box
                        self.is_listening = False  # Stop after one successful recognition
                        
                        # Update UI in main thread
                        self.voice_button.setText("🎙 Voice Mode")
                        self.voice_button.setStyleSheet("""
                            QPushButton {
                                background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.8, 
                                                            fx:0.5, fy:0.5, stop:0 #ff0000, stop:1 #8b0000);
                                color: white;
                                border-radius: 110px;
                                border: 5px solid #ff4444;
                                font-size: 20px;
                            }
                        """)
                    except sr.WaitTimeoutError:
                        print("Listening timed out...")
                        continue
                    except sr.UnknownValueError:
                        print("Could not understand audio")
                        continue
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
                        continue
        except Exception as e:
            print(f"Error in voice recognition: {e}")
            self.is_listening = False

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