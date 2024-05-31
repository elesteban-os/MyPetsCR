
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Interfaz.ventanas.Citas import VentanaCitasAdmi
from Interfaz.ventanas.admicitas import AdmicitasWindow
from ventanas.Login import Login
from ventanas.registro import RegistrarUsuario
from ventanas.cliente import ClienteWindow
from ventanas.administrador import AdministradorWindow
from ventanas.veterinario import VeterinarioWindow
from ventanas.Inicio import Inicializar
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicio_window = Inicializar(self)
        self.login_window = Login(self)
        self.registro_window = RegistrarUsuario(self)
        self.cliente_window = ClienteWindow()
        self.administrador_window = AdministradorWindow()
        self.veterinario_window = VeterinarioWindow()
        self.admicitas_window = AdmicitasWindow()
        self.show_inicio_window()

    def show_inicio_window(self):
        self.inicio_window.show()

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
        
    def show_Citas_Admi_window(self):
        self.admicitas_window.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
