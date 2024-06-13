import sys
import json
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont

class ReviewApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Datos1_Proyecto1/MyPetsCR/Interfaz/ReviewP.ui", self)

        self.pushButton.clicked.connect(self.close)  # Botón Cancelar
        
        # Cargar reseñas desde el archivo JSON
        with open('C:/Datos1_Proyecto1/MyPetsCR/Interfaz/ReviewP.json', 'r', encoding='utf-8') as f:
            self.reviews_data = json.load(f)
        
        # Configurar el ListWidget para mostrar las reseñas
        for review in self.reviews_data:
            # Crear un nuevo widget para cada reseña
            review_widget = QWidget()
            layout = QHBoxLayout()
            review_widget.setLayout(layout)
            
            # Crear un widget para los detalles de la reseña
            details_widget = QWidget()
            details_layout = QVBoxLayout()
            details_widget.setLayout(details_layout)
            
            # Añadir los detalles de la reseña (Producto, Usuario, Calificación, Comentario)
            product_label = QLabel(f'<b>Producto:</b> {review["Producto"]}')
            user_label = QLabel(f'<b>Usuario:</b> {review["Nombre"]}')
            rating_label = QLabel(f'<b>Calificación:</b> {review["Calificación"]}')
            comment_label = QLabel(f'<b>Comentario:</b> {review["Comentario"]}')
            
            # Configurar el espaciado y la fuente para los labels
            font = QFont()
            font.setPointSize(12)
            product_label.setFont(font)
            user_label.setFont(font)
            rating_label.setFont(font)
            comment_label.setFont(font)
            
            details_layout.addWidget(product_label)
            details_layout.addWidget(user_label)
            details_layout.addWidget(rating_label)
            details_layout.addWidget(comment_label)
            
            # Agregar el widget de detalles al layout horizontal
            layout.addWidget(details_widget)
            
            # Añadir la imagen del producto si está disponible
            if 'Imagen' in review:
                image_label = QLabel()
                pixmap = QPixmap(review['Imagen'])
                # Ajustar tamaño de la imagen para que no sea demasiado grande
                pixmap = pixmap.scaledToWidth(150)  # Ajustar el ancho según sea necesario
                image_label.setPixmap(pixmap)
                layout.addWidget(image_label)
            
            # Añadir el widget de reseña al QListWidget
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(review_widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, review_widget)
        
        # Mostrar la ventana principal
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviewApp()
    sys.exit(app.exec_())
