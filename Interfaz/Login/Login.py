from PyQt6 import QtWidgets,uic
#Iniciar la aplicacion
app = QtWidgets.QAplication([])

#Cargar archvivos.iu

login= uic.loadUi("Ventana2.ui")
entrar = uic.loadUi("Ventana3.ui")
error = uic.loadUi("ventana4.ui")

#Ejecutable
login.show()
app.exe()