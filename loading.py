import sys
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
import text_analyzer  # Assuming this is a module you already have


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Loading Screen')
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: black; border-radius: 10px;")

        # Layout
        layout = QVBoxLayout(self)

        # Title or message
        self.loading_label = QLabel("LOADING MODEL Please Wait", self)
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_label.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        
        # Progress Bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: black;
                border-radius: 5px;
                height: 25px;
                color: red;
            }
            QProgressBar::chunk {
                background-color: cyan;
                border-radius: 5px;
            }
        """)

        layout.addWidget(self.loading_label)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        # Timer to simulate loading
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_loading)
        self.timer.start(50)  # Update every 50ms

        self.progress = 0  # To simulate loading progress

    def update_loading(self):
        self.progress += 1
        if self.progress > 100:
            self.progress = 100
            self.timer.stop()
        
        self.progress_bar.setValue(self.progress)


class ModelLoaderThread(QThread):
    progress_signal = pyqtSignal(int)
    model_loaded_signal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        # Simulate model loading by updating progress
        for i in range(101):
            self.progress_signal.emit(i)
            # Simulate some time for loading
            QThread.msleep(50)  # Adjust time based on real model loading time

        # Now run the model loading (this should be non-blocking)
        text_analyzer.process_command("sample")  # Replace with your actual model loading logic
        
        # Once model is loaded, signal the main application
        self.model_loaded_signal.emit()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Window Settings
        self.setWindowTitle("AI Task Automation - Main UI")
        self.setGeometry(100, 100, 850, 550)
        self.setStyleSheet("background-color: #121212;")  # Dark Theme

        # Main Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Header Label
        self.header_label = QLabel("AI Task Automation")
        self.header_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.header_label.setStyleSheet("color: white; margin-bottom: 20px;")
        self.header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.header_label)
        
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    # Show loading screen
    loading_screen = LoadingScreen()
    loading_screen.show()

    # Create and start the model loading thread
    loader_thread = ModelLoaderThread()
    loader_thread.progress_signal.connect(loading_screen.progress_bar.setValue)
    loader_thread.model_loaded_signal.connect(lambda: on_model_loaded(loading_screen))

    loader_thread.start()

    sys.exit(app.exec())


def on_model_loaded(loading_screen):
    loading_screen.close()  # Close the loading screen
    main_window = MainWindow()
    main_window.show()


if __name__ == "__main__":
    main()