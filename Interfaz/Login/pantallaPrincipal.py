from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic






class Ventana5(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("Ventana5.ui", self)