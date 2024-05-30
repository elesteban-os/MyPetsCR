from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
from Login import Login
from Tienda import Tienda

class Inicializar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Ventana0.ui", self)

        # Conectar el botón pushButton al método show_login
        self.pushButton.clicked.connect(self.show_login)
        self.pushButton_2.clicked.connect(self.show_tienda)

    def show_login(self):
        self.login_window = Login()
        self.login_window.show()

    def show_tienda(self):
        self.tienda_window = Tienda()
        self.tienda_window.show()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Inicializar()
    window.show()
    sys.exit(app.exec())