import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt
from .ProductosTienda import ProductosTienda
from .EliminarProductos import EliminarProductos
class VentanaAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configuración básica de la ventana
        self.setWindowTitle('Ventana Administrador')
        self.setGeometry(100, 100, 600, 400)  # Posición x, posición y, ancho, alto
        
        # Crear widget central para contener los botones
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: white; color: black;")
        self.setCentralWidget(central_widget)
        
        # Crear layout vertical
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Agregar título al layout
        titulo = QLabel('Selecciona una opción', self)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)
        
        # Crear espacio para centrar verticalmente
        vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(vertical_spacer)
        
        # Agregar botones al layout
        boton1 = QPushButton('Botón 1', self)
        boton1.setFixedSize(100, 30)  # Ancho, alto
        layout.addWidget(boton1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        boton1.clicked.connect(self.boton1_clicked) 

        boton2 = QPushButton('Botón 2', self)
        boton2.setFixedSize(100, 30)  # Ancho, alto
        layout.addWidget(boton2, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        boton2.clicked.connect(self.boton2_clicked)  
        
        # Añadir espacio para centrar verticalmente
        layout.addItem(vertical_spacer)

    def boton1_clicked(self):
        self.productos_window = ProductosTienda()
        self.productos_window.show()

    def boton2_clicked(self):
        self.eliminar_window = EliminarProductos()
        self.eliminar_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentanaAdmin()
    window.show()
    sys.exit(app.exec())

