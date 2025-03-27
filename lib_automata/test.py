import sys
import warnings
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QLabel, QProgressBar, QTextEdit)
from PyQt6.QtCore import QThread, pyqtSignal, QObject, QTimer
from PyQt6.QtGui import QTextCursor

# Suppress warnings initially
warnings.filterwarnings("ignore")

class ModelLoader(QObject):
    finished = pyqtSignal(object)
    log_message = pyqtSignal(str)
    progress_update = pyqtSignal(str)

    def load_model(self):
        try:
            self.log_message.emit("Preparing to load model...")
            
            # Import inside thread to delay heavy imports
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                from transformers import pipeline
            
            self.progress_update.emit("Downloading model files...")
            self.log_message.emit("This may take a few minutes...")
            
            # Load the actual model
            nlp = pipeline("fill-mask", model="distilroberta-base")
            
            self.progress_update.emit("Model loaded successfully!")
            self.finished.emit(nlp)
        except Exception as e:
            self.log_message.emit(f"Error loading model: {str(e)}")
            self.finished.emit(None)

class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Model Loading")
        self.setGeometry(300, 300, 500, 300)
        
        layout = QVBoxLayout()
        
        self.status_label = QLabel("Initializing...")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)  # Indeterminate mode
        
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        
        layout.addWidget(self.status_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(QLabel("Loading Logs:"))
        layout.addWidget(self.log_output)
        
        self.setLayout(layout)
    
    def update_status(self, message):
        self.status_label.setText(message)
        self.repaint()
    
    def log_message(self, message):
        self.log_output.append(message)
        self.log_output.moveCursor(QTextCursor.MoveOperation.End)
        self.repaint()

def main():
    # Create application and show window immediately
    app = QApplication(sys.argv)
    window = LoadingWindow()
    window.show()
    
    # Force GUI to appear before loading starts
    app.processEvents()
    
    # Set up the worker thread
    thread = QThread()
    worker = ModelLoader()
    worker.moveToThread(thread)
    
    # Connect signals
    worker.progress_update.connect(window.update_status)
    worker.log_message.connect(window.log_message)
    worker.finished.connect(thread.quit)
    
    def handle_finished(nlp):
        window.close()
        if nlp is not None:
            start_terminal_interface(nlp)
        else:
            print("Failed to load model. Exiting.")
            sys.exit(1)
    
    worker.finished.connect(handle_finished)
    
    # Start the thread after a small delay to ensure GUI is visible
    QTimer.singleShot(100, thread.start)
    thread.started.connect(worker.load_model)
    
    # Run the application
    app.exec()

def start_terminal_interface(nlp):
    print("\nModel loaded successfully! You can now interact with it.")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            text = input("Enter a masked sentence (e.g. 'Hello <mask> world!'): ")
            if text.lower() == 'exit':
                break
            results = nlp(text)
            for result in results:
                print(f"{result['sequence']} (score: {result['score']:.4f})")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()