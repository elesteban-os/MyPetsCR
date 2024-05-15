'''from PyQt6 import QtWidgets,uic
from PyQt6.QtWidgets import QApplication, QMainWindow
#Iniciar la aplicacion
app = QtWidgets.QApplication([])

#Cargar archvivos.iu

login= uic.loadUi("Ventana2.ui")
entrar = uic.loadUi("Ventana3.ui")
error = uic.loadUi("ventana4.ui")

def gui_login():
    name = login.lineEdit.text() 
    password = login.lineEdit_2.text()
    if len(name) == 0 or len(password) ==0:
        login.label_7.setText("Ingrese todos los datos porfavor")
    elif name == "Mei" and password =="1234":
        gui_entrar()
    else:
        gui_error() 

    
def gui_entrar():
    login.hide()
    entrar.show()
def gui_error():
    login.hide()
    error.show()

def regresar_entrar():
    entrar.hide()
    login.label_7.setText("")
    login.show()

def regresar_error():
    error.hide()
    login.label_7.setText("")
    login.show()
def salir():
    app.exit()
#Botones Funciones
login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(salir)

entrar.pushButton.clicked.connect(regresar_entrar)
entrar.pushButton_2.clicked.connect(salir)

error.pushButton.clicked.connect(regresar_error)
error.pushButton_2.clicked.connect(salir)

#Ejecutable
login.show()
app.exec()'''
