from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class VeterinarioWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Ventana8.ui", self)
