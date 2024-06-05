import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Ventana7.ui", self)
        self.pushButton_8.clicked.connect(self.abrir_ventana_secundaria)
        self.pushButton_9.clicked.connect(self.close)

    def abrir_ventana_secundaria(self):
        from citasadmin import VentanaCitasAdmi
        self.ventana_citas_admi = VentanaCitasAdmi()
        self.ventana_citas_admi.show()

class VentanaCitasAdmi(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\Citas_Admi_ui.py", self)
        self.pushButton.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    sys.exit(app.exec_())
