from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class ClienteWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Ventana5.ui", self)

