
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ventanas.Login import Login

from ventanas.cliente import ClienteWindow
from ventanas.administrador import AdministradorWindow
from ventanas.veterinario import VeterinarioWindow
from ventanas.Inicio import Inicializar
from ventanas.Tienda import Tienda

#deberíamos hacer que cuando se toque la X de arriba (la que sale n rojo siempre) 
#se cierre todo el programa y q nada más cada ventana se pueda hacer para atras(algunas ya tienen eso de hacerse para atras pero lo de la x roja habría que hacerlo)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicio_window = Inicializar(self)
        self.login_window = Login(self)
        self.cliente_window = ClienteWindow()
        self.administrador_window = AdministradorWindow()
        self.veterinario_window = VeterinarioWindow()
        self.tienda_window = Tienda(self)
        self.show_inicio_window()

    def show_inicio_window(self):
        self.inicio_window.show()

    def show_tienda_window(self):
        self.tienda_window.show()

    def show_login_window(self):
        self.login_window.show()

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
