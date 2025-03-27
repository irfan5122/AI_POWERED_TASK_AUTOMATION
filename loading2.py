import sys
import os
from PyQt6.QtCore import Qt, QThread, pyqtSignal, QTimer, QPropertyAnimation
from PyQt6.QtGui import QColor, QLinearGradient, QPainter, QFont
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QLabel, QProgressBar, QGraphicsDropShadowEffect)

# Suppress TensorFlow/PyTorch logs initially
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings("ignore")

class ModelLoaderThread(QThread):
    progress_updated = pyqtSignal(int, str)
    loading_complete = pyqtSignal()

    def run(self):
        self.progress_updated.emit(10, "Preparing system...")
        
        # Import model components only after GUI is shown
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            from transformers import pipeline
            import text_analyzer
            
        self.progress_updated.emit(30, "Loading neural network...")
        text_analyzer.nlp = pipeline("fill-mask", model="distilroberta-base")
        
        # Simulate remaining loading
        for progress in range(40, 101, 10):
            QThread.msleep(150)
            self.progress_updated.emit(progress, f"Initializing components... {progress}%")
        
        self.loading_complete.emit()

class FuturisticLoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.show()
        QApplication.processEvents()  # Force immediate GUI display
        
        # Start loading after GUI is definitely visible
        QTimer.singleShot(100, self.start_model_loading)

    def setup_ui(self):
        self.setWindowTitle("AI Initialization")
        self.setFixedSize(600, 300)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Container with shadow
        container = QWidget(self)
        container.setGeometry(0, 0, 600, 300)
        container.setStyleSheet("""
            background-color: rgba(10, 15, 25, 220);
            border-radius: 15px;
            border: 1px solid rgba(100, 180, 255, 50);
        """)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(100, 180, 255, 150))
        shadow.setOffset(0, 0)
        container.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # UI Elements
        self.title = QLabel("SYSTEM BOOTING")
        self.title.setStyleSheet("""
            color: #00e5ff;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 2px;
        """)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setStyleSheet("""
            QProgressBar {
                background: rgba(30, 40, 60, 200);
                border-radius: 6px;
                height: 12px;
            }
            QProgressBar::chunk {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,
                    stop:0 #00e5ff, stop:0.5 #6200ea, stop:1 #00e5ff
                );
                border-radius: 6px;
            }
        """)
        
        self.status = QLabel("Initializing...")
        self.status.setStyleSheet("color: rgba(200, 220, 255, 180); font-family: 'Consolas';")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(self.title)
        layout.addWidget(self.progress)
        layout.addWidget(self.status)

    def start_model_loading(self):
        self.loader_thread = ModelLoaderThread()
        self.loader_thread.progress_updated.connect(self.update_progress)
        self.loader_thread.loading_complete.connect(self.on_loaded)
        self.loader_thread.start()

    def update_progress(self, value, message):
        self.progress.setValue(value)
        self.status.setText(message)
        QApplication.processEvents()

    def on_loaded(self):
        self.close()
        # Launch your main window here

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(10, 20, 40, 150))
        gradient.setColorAt(1, QColor(5, 10, 20, 150))
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(self.rect())

def show_loading_screen():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = FuturisticLoadingScreen()
    app.exec()

if __name__ == "__main__":
    show_loading_screen()