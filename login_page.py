import sys
import os
from enc_dec import encrypt_file, decrypt_file
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont, QColor, QGuiApplication
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 500, 300)  
        self.setStyleSheet("background-color: #1e1e1e;")  

        # Center the window
        self.center()

        # Username Label
        username_label = QLabel("USERNAME :")
        username_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        username_label.setStyleSheet("color: #00bcd4;")

        self.username_input = QLineEdit()
        self.username_input.setFixedHeight(35)
        self.username_input.setStyleSheet("background-color: #2e2e2e; color: white; border-radius: 10px; padding: 5px;")

        # Password Label
        password_label = QLabel("PASSWORD:")
        password_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        password_label.setStyleSheet("color: #00bcd4;")

        self.password_input = QLineEdit()
        self.password_input.setFixedHeight(35)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: #2e2e2e; color: white; border-radius: 10px; padding: 5px;")

        # Buttons
        login_button = QPushButton("LOGIN")
        login_button.setFixedSize(120, 40)
        login_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        login_button.setStyleSheet("""
            QPushButton {
                background-color: #00bcd4;
                color: white;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #008c8c;
            }
        """)
        login_button.clicked.connect(self.on_login)

        create_account_button = QPushButton("Create Account")
        create_account_button.setFixedSize(140, 40)
        create_account_button.setFont(QFont("Arial", 12))
        create_account_button.setStyleSheet("""
            QPushButton {
                background-color: #008c8c;
                color: white;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #006666;
            }
        """)
        create_account_button.clicked.connect(self.on_signup)

        # Layouts
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addSpacing(20)

        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(create_account_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def center(self):
        """ Center the window on the screen """
        screen = QGuiApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        self.move(
            (screen.width() - window_geometry.width()) // 2,
            (screen.height() - window_geometry.height()) // 2
        )

    def on_login(self):
        username_box = self.username_input.text().strip()
        password_box = self.password_input.text().strip()

        if os.path.exists("user_data.apta"):
            decrypt_file()

        if username_box and password_box:
            try:
                with open("user_data", "r") as file:
                    username, password = file.readline().strip().split(",")
                    
                if username_box == username and password_box == password:
                    print("Logged in Successfully")
                    self.hide()
                    from loading import FuturisticLoadingScreen
                    self.loading_screen = FuturisticLoadingScreen()
                    self.loading_screen.loading_complete.connect(self.show_main_window)
                    self.loading_screen.show()
                    
                    
                else:
                    QMessageBox.warning(self, "Login Failed", "Incorrect Username or Password")
            except FileNotFoundError:
                QMessageBox.warning(self, "Warning", "Account Does Not Exist!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Login failed: {str(e)}")
        else:
            QMessageBox.warning(self, "Warning", "Please enter both username and password!")

    def show_main_window(self):
        self.loading_screen.close()
        from main import ModernAdvancedUI
        self.main_window = ModernAdvancedUI()
        self.main_window.show()
        
    def on_signup(self):
        """ Open the Create Account window """
        self.close()
        self.signup_window = SignupWindow()
        self.signup_window.show()


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Create Account")
        self.setGeometry(100, 100, 500, 350)  
        self.setStyleSheet("background-color: #1e1e1e;")  

        self.center()

        # Username Label
        username_label = QLabel("New Username:")
        username_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        username_label.setStyleSheet("color: #00bcd4;")

        self.username_input = QLineEdit()
        self.username_input.setFixedHeight(35)
        self.username_input.setStyleSheet("background-color: #2e2e2e; color: white; border-radius: 10px; padding: 5px;")

        # Password Label
        password_label = QLabel("New Password:")
        password_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        password_label.setStyleSheet("color: #00bcd4;")

        self.password_input = QLineEdit()
        self.password_input.setFixedHeight(35)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("background-color: #2e2e2e; color: white; border-radius: 10px; padding: 5px;")

        # Create Account Button
        create_button = QPushButton("Create Account")
        create_button.setFixedSize(160, 40)
        create_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        create_button.setStyleSheet("""
            QPushButton {
                background-color: #00bcd4;
                color: white;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #008c8c;
            }
        """)
        create_button.clicked.connect(self.on_create_account)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4444;
                color: white;
                border-radius: 20px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        back_button.clicked.connect(self.go_back)

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addSpacing(20)

        button_layout = QHBoxLayout()
        button_layout.addWidget(back_button)
        button_layout.addWidget(create_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def center(self):
        screen = QGuiApplication.primaryScreen().geometry()
        window_geometry = self.frameGeometry()
        self.move(
            (screen.width() - window_geometry.width()) // 2,
            (screen.height() - window_geometry.height()) // 2
        )

    def on_create_account(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if username and password:

            filename = "user_data.apta"
            if not os.path.exists(filename):
                with open("user_data",'w') as data:
                    data.write(f"{username},{password}")
                encrypt_file()
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Account Created")
                msg_box.setText("Account Created Successfully")
                msg_box.setIcon(QMessageBox.Icon.Information)
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.exec()

            else:
                msg_box = QMessageBox() 
                msg_box.setWindowTitle("WARNING")  
                msg_box.setText("Account Already Exists !") 
                msg_box.setIcon(QMessageBox.Icon.Information)  
                msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg_box.exec()
            self.go_back()
        else:
            print("Please enter both username and password!")

    def go_back(self):
        """ Return to the Login Window """
        self.close()
        self.login_window = LoginWindow()
        self.login_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    flag = 0  

    if flag == 0:
        window = LoginWindow()
    else:
        window = SignupWindow()

    window.show()
    sys.exit(app.exec())