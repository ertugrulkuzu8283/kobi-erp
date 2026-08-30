import sys
from collections.abc import Callable
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget, 
    QVBoxLayout, QLabel, QPushButton, QLineEdit
)


class LoginWindow(QWidget):
    def __init__(self, switch_callback: Callable[[], None]):
        super().__init__()
        self.setWindowTitle("KOBİ ERP - Giriş")
        self.resize(300, 200)
        
        layout = QVBoxLayout()
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Kullanıcı Adı")
        
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Şifre")
        self.pass_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        login_btn = QPushButton("Giriş Yap")
        login_btn.clicked.connect(switch_callback)
        
        layout.addWidget(QLabel("KOBİ ERP Kimlik Doğrulama"))
        layout.addWidget(self.user_input)
        layout.addWidget(self.pass_input)
        layout.addWidget(login_btn)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("KOBİ ERP - Ana Konsol")
        self.resize(800, 600)
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Navigasyon Kabuğu (Navigation Shell) Aktif"))
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class AppController:
    def __init__(self):
        self.stack = QStackedWidget()
        self.login_win = LoginWindow(self.show_main)
        self.main_win = MainWindow()
        
        self.stack.addWidget(self.login_win)
        self.stack.addWidget(self.main_win)
        self.stack.setCurrentWidget(self.login_win)
        self.stack.resize(800, 600)
        self.stack.show()

    def show_main(self) -> None:
        self.stack.setCurrentWidget(self.main_win)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())