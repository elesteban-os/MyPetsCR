
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys 
import re
import sqlite3
from registrarUsuario import RegisterWindow

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventana2.ui", self)

        #Aquí van los botones
         # Accede al QComboBox y agrega las opciones
        self.comboBox.addItems(["Administrador", "Veterinario", "Cliente"])

        # Conecta el botón de salir con la función para cerrar la aplicación
        self.pushButton_2.clicked.connect(self.close_application)

        # Conecta el botón de registro
        self.pushButton_3.clicked.connect(self.open_register_window)

        # Conecta la señal currentIndexChanged del QComboBox al método toggle_register_button
        self.comboBox.currentIndexChanged.connect(self.toggle_register_button)

        # Conecta el botón de inicio de sesión
        self.pushButton.clicked.connect(self.login_user)

        # Inicialmente, oculta el botón de registro
        self.pushButton_3.setVisible(False)

    def close_application(self):
        QApplication.quit()

    def open_register_window(self):
        self.register_window = RegisterWindow(self)
        self.register_window.show()
        self.hide()


    def login_user(self):
        # Implementar lógica
        pass
    def toggle_register_button(self):
        user_type = self.comboBox.currentText()
        if user_type == "Administrador":
            self.pushButton_3.setVisible(True)
        else:
            self.pushButton_3.setVisible(False)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())


