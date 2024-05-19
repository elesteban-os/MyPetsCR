from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
from Login import Login

class Inicializar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventana0.ui", self)

        # Conectar el botón pushButton al método show_login
        self.pushButton.clicked.connect(self.show_login)

    def show_login(self):
        self.login_window = Login()
        self.login_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicializar()
    window.show()
    sys.exit(app.exec())