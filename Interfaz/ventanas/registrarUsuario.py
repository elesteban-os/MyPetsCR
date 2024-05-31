from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
import sys
import sqlite3

class FormularioRegistro(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        uic.loadUi("Ventana6.ui", self)

       # self.pushButton.clicked.connect(self.registrar_cliente)
        self.pushButton_2.clicked.connect(self.volver_a_pagina_administrador)

    def volver_a_pagina_administrador(self):
        if self.parent_window is not None:
            self.parent_window.show()
        self.close()



#if __name__ == "__main__":
  #  app = QApplication(sys.argv)
  #  window = FormularioRegistro()
   # window.show()
  #  sys.exit(app.exec())
