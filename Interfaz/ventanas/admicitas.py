from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

class AdmicitasWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Citas_Admi.ui", self)

