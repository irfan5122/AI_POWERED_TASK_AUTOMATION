import sys
import os
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal, QPropertyAnimation
from PyQt6.QtGui import QColor, QLinearGradient, QPainter, QFont
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QLabel, QProgressBar, QGraphicsDropShadowEffect)

# Suppress initial warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings
warnings.filterwarnings("ignore")

class ModelLoader(QThread):
    progress_updated = pyqtSignal(int, str)
    loading_complete = pyqtSignal()

    def run(self):
        self.progress_updated.emit(10, "Initializing system...")
        
        # Import and load model after GUI is shown
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            from transformers import pipeline
            import text_analyzer
            
        self.progress_updated.emit(30, "Loading AI model...")
        text_analyzer.nlp = pipeline("fill-mask", model="distilroberta-base")
        
        # Simulate remaining loading
        for progress in range(40, 101, 10):
            QThread.msleep(200)
            self.progress_updated.emit(progress, f"Loading components... {progress}%")
        
        self.loading_complete.emit()

class FuturisticLoadingScreen(QWidget):
    loading_complete = pyqtSignal()
    def __init__(self):
        super().__init__()
        # Keep your exact UI setup
        self.setWindowTitle("System Initialization")
        self.setFixedSize(600, 300)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Main container
        self.container = QWidget(self)
        self.container.setGeometry(0, 0, 600, 300)
        self.container.setStyleSheet("""
            background-color: rgba(10, 15, 25, 220);
            border-radius: 15px;
            border: 1px solid rgba(100, 180, 255, 50);
        """)
        
        # Add drop shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(100, 180, 255, 150))
        shadow.setOffset(0, 0)
        self.container.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(30)
        
        # Title with animation
        self.title = QLabel("SYSTEM INITIALIZATION")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet("""
            color: #4fc3f7;
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 2px;
        """)
        
        # Progress bar
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(12)
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: rgba(30, 40, 60, 200);
                border-radius: 6px;
                border: 1px solid rgba(100, 180, 255, 30);
            }
            QProgressBar::chunk {
                background-color: qlineargradient(
                    spread:pad, x1:0, y1:0.5, x2:1, y2:0.5,
                    stop:0 #00e5ff, stop:0.5 #6200ea, stop:1 #00e5ff
                );
                border-radius: 6px;
            }
        """)
        
        # Status text
        self.status = QLabel("Starting system...")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status.setStyleSheet("""
            color: rgba(200, 220, 255, 180);
            font-size: 14px;
            font-family: 'Consolas';
        """)
        
        # Percentage indicator
        self.percentage = QLabel("0%")
        self.percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.percentage.setStyleSheet("""
            color: #00e5ff;
            font-size: 18px;
            font-weight: bold;
        """)
        
        layout.addWidget(self.title)
        layout.addWidget(self.progress)
        layout.addWidget(self.status)
        layout.addWidget(self.percentage)
        
        # Pulsing title animation
        self.title_animation = QPropertyAnimation(self.title, b"styleSheet")
        self.title_animation.setDuration(2000)
        self.title_animation.setLoopCount(-1)
        self.title_animation.setKeyValueAt(0, "color: #4fc3f7; font-size: 24px;")
        self.title_animation.setKeyValueAt(0.5, "color: #00e5ff; font-size: 25px;")
        self.title_animation.setKeyValueAt(1, "color: #4fc3f7; font-size: 24px;")
        self.title_animation.start()
        
        # Show immediately
        self.show()
        QApplication.processEvents()
        
        # Start model loading after short delay
        QTimer.singleShot(100, self.start_loading)

    def start_loading(self):
        self.loader = ModelLoader()
        self.loader.progress_updated.connect(self.update_progress)
        self.loader.loading_complete.connect(self.loading_finished)
        self.loader.start()

    def update_progress(self, value, message):
        self.progress.setValue(value)
        self.percentage.setText(f"{value}%")
        self.status.setText(message)
        QApplication.processEvents()

    def loading_finished(self):
        self.close()
        from main import ModernAdvancedUI
        self.main_window = ModernAdvancedUI()
        self.main_window.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(10, 20, 40, 150))
        gradient.setColorAt(1, QColor(5, 10, 20, 150))
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(self.rect())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = FuturisticLoadingScreen()
    app.exec()