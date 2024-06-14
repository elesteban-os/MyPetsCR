import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QGridLayout, QFrame
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QSize
from PIL import Image

# Lista de rutas de imágenes
imagenes = [
    "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\central.jpg",
    "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\norte.jpg",
    "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\sur.jpg",
    "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\este.jpg",
    "C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\oeste.jpg",
    r"C:\\Datos1_Proyecto1\\MyPetsCR\\Interfaz\\Imagenes\\fondo_nuestrastiendas.jpeg"
]

# Convertir imágenes a un formato estándar sin perfiles ICC
for imagen in imagenes:
    with Image.open(imagen) as img:
        img = img.convert("RGB")  # Convertir a RGB
        img.save(imagen, format="JPEG", icc_profile=None)  # Guardar sin perfil ICC

class SedeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana principal
        self.setWindowTitle('Nuestras Tiendas')
        self.setGeometry(100, 100, 800, 600)

        # Imagen de fondo
        fondo = imagenes[5]  # Reemplaza con la ruta de tu imagen de fondo
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)
        self.set_background(fondo)

        # Widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("background: transparent;")

        # Layout principal de la ventana
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        # Título
        titulo = QLabel('Nuestras tiendas están ubicadas en los siguientes lugares del país:')
        titulo.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: black;")  # Set text color to black
        layout.addWidget(titulo)

        # Crear un grid layout para las imágenes y las sedes
        grid_layout = QGridLayout()
        grid_layout.setSpacing(20)

        # Lista de lugares, imágenes y direcciones (debes reemplazar las rutas de las imágenes por las tuyas)
        lugares = [
            ("Central", imagenes[0], "Avenida Central, Edificio Central, San José"),
            ("Norte", imagenes[1], "Calle 10, Barrio Norte, Heredia"),
            ("Sur", imagenes[2], "Avenida Sur, Plaza del Sur, Cartago"),
            ("Este", imagenes[3], "Boulevard Este, Centro Comercial Este, San Pedro"),
            ("Oeste", imagenes[4], "Ruta 27, Centro Empresarial Oeste, Escazú")
        ]

        for i, (sede, imagen, direccion) in enumerate(lugares):
            # Crear un frame para cada sede
            frame = QFrame()
            frame.setFrameShape(QFrame.Shape.Box)
            frame.setLineWidth(2)
            frame.setStyleSheet("background-color: #FFFFFF;")  # Fondo blanco para los frames
            frame_layout = QVBoxLayout()
            frame_layout.setContentsMargins(10, 10, 10, 10)

            # Etiqueta de la sede
            label_sede = QLabel(sede)
            label_sede.setFont(QFont('Arial', 14, QFont.Weight.Bold))
            label_sede.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_sede.setStyleSheet("color: black;")  # Set text color to black
            frame_layout.addWidget(label_sede)

            # Imagen de la sede
            label_imagen = QLabel()
            pixmap = QPixmap(imagen).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            label_imagen.setPixmap(pixmap)
            label_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
            frame_layout.addWidget(label_imagen)

            # Dirección de la sede
            label_direccion = QLabel(direccion)
            label_direccion.setFont(QFont('Arial', 12))
            label_direccion.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label_direccion.setStyleSheet("color: black;")  # Set text color to black
            frame_layout.addWidget(label_direccion)

            frame.setLayout(frame_layout)
            grid_layout.addWidget(frame, i // 2, i % 2)

        layout.addLayout(grid_layout)

        # Asegurar que el fondo se redimensione con la ventana
        self.centralWidget().resizeEvent = self.resize_background

    def set_background(self, path):
        pixmap = QPixmap(path)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

    def resize_background(self, event):
        self.background_label.setGeometry(0, 0, event.size().width(), event.size().height())
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = SedeWindow()
    main_window.show()
    sys.exit(app.exec())



