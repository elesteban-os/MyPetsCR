import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ventanas.Login import Login
from ventanas.registro import RegistrarUsuario
from ventanas.cliente import ClienteWindow
from ventanas.administrador import AdministradorWindow
from ventanas.veterinario import VeterinarioWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login_window = Login(self)
        self.registro_window = RegistrarUsuario(self)
        self.cliente_window = ClienteWindow()
        self.administrador_window = AdministradorWindow()
        self.veterinario_window = VeterinarioWindow()
        self.show_login_window()

    def show_login_window(self):
        self.login_window.show()

    def show_registro_window(self):
        self.registro_window.show()

    def show_cliente_window(self):
        self.cliente_window.show()

    def show_administrador_window(self):
        self.administrador_window.show()

    def show_veterinario_window(self):
        self.veterinario_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
