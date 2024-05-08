from PyQt6 import QtWidgets, uic

class LoginW(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventana2.ui", self)    #Carga ventana del login no se si es la 2 jajaja

        self.login_button.clicked.connect(self.handle_login) #Cuando se precione el btn llama a la funcion

    def handle_login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()

        # Autenticación  comprobación de credenciales
        if username == 'admin' and password == 'admin':
            self.status_label.setText('Inicio de sesión exitoso')
        else:
            self.status_label.setText('Nombre de usuario o contraseña incorrectos')

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = LoginW()
    window.show()
    app.exec()