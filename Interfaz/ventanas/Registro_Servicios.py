import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Registro_Servicios.ui", self)

        # Conectar botones a funciones
        self.btn_agregar.clicked.connect(self.mostrarMensaje)
        self.btn_salir.clicked.connect(self.salirVentana)

    def mostrarMensaje(self):
        QMessageBox.information(self, "Mensaje", "¡Agregado correctamente!")

    def salirVentana(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
