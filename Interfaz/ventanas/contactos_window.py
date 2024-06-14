import sys
from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QApplication, QMessageBox
from PyQt6.QtGui import QDesktopServices, QPixmap, QPalette, QBrush
from PyQt6.QtCore import QUrl, Qt

class ContactWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contactos de la Veterinaria")
        self.setGeometry(100, 100, 800, 600)
        
        # Crear un layout
        layout = QVBoxLayout()
        
        # Estilo común para los labels con texto blanco
        white_text_label_style = """
        QLabel {
            font-size: 18px;
            padding: 10px;
            background-color: rgba(0, 0, 0, 150);
            border-radius: 10px;
            color: white;
        }
        QLabel a {
            color: white;
            text-decoration: none;
        }
        QLabel a:hover {
            text-decoration: underline;
        }
        """
        
        # Estilo para el número de teléfono con texto negro
        phone_label_style = """
        QLabel {
            font-size: 18px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 180);
            border-radius: 10px;
            color: black;
        }
        """
        
        # Contacto de WhatsApp
        self.whatsapp_label = QLabel(
            "<img src='C:\\Users\\Meibel\\Downloads\\MyPetsCR-main (2)\\MyPetsCR-main\\Interfaz\\Imagenes\\whatsapp.png' width='50' height='50'> "
            "<span>WhatsApp: <a href='https://wa.me/11234567890'>Enviar mensaje</a></span>"
        )
        self.whatsapp_label.setOpenExternalLinks(True)
        self.whatsapp_label.setStyleSheet(white_text_label_style)
        layout.addWidget(self.whatsapp_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Contacto correos electrónicos
        self.gmail_label = QLabel(
            "<img src='C:\\Users\\Meibel\\Downloads\\MyPetsCR-main (2)\\MyPetsCR-main\\Interfaz\\Imagenes\\gmail.png' width='30' height='30'> "
            "<span>Correo Gmail: <a href='#' id='gmail'>veterinariaMiPet@gmail.com</a></span>"
        )
        self.gmail_label.linkActivated.connect(self.open_gmail)
        self.gmail_label.setStyleSheet(white_text_label_style)
        layout.addWidget(self.gmail_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.outlook_label = QLabel(
            "<img src='C:\\Users\\Meibel\\Downloads\\MyPetsCR-main (2)\\MyPetsCR-main\\Interfaz\\Imagenes\\outlook1.png' width='30' height='30'> "
            "<span>Correo Outlook: <a href='#' id='outlook'>veterinariasMiPet@outlook.com</a></span>"
        )
        self.outlook_label.linkActivated.connect(self.open_outlook)
        self.outlook_label.setStyleSheet(white_text_label_style)
        layout.addWidget(self.outlook_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Número de teléfono
        self.phone_label = QLabel("Teléfono: +123 456 7890")
        self.phone_label.setStyleSheet(phone_label_style)
        layout.addWidget(self.phone_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Redes sociales
        self.facebook_label = QLabel(
            "<img src='C:\\Users\\Meibel\\Downloads\\MyPetsCR-main (2)\\MyPetsCR-main\\Interfaz\\Imagenes\\facebook.png' width='80' height='50'> "
            "<span>Facebook: <a href='https://www.facebook.com/tu_pagina'>Mi_Pet_Veterinaria</a></span>"
        )
        self.facebook_label.setOpenExternalLinks(True)
        self.facebook_label.setStyleSheet(white_text_label_style)
        layout.addWidget(self.facebook_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.instagram_label = QLabel(
            "<img src='C:\\Users\\Meibel\\Downloads\\MyPetsCR-main (2)\\MyPetsCR-main\\Interfaz\\Imagenes\\instagram.png' width='50' height='50'> "
            "<span>Instagram: <a href='https://www.instagram.com/tu_pagina'>MiPet_veterinarias</a></span>"
        )
        self.instagram_label.setOpenExternalLinks(True)
        self.instagram_label.setStyleSheet(white_text_label_style)
        layout.addWidget(self.instagram_label, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Ventana Principal
        central_widget = QWidget()
        central_widget.setLayout(layout)
        
        # Añadir fondo de pantalla
        self.setCentralWidget(central_widget)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap("C:/Users/Meibel/Downloads/MyPetsCR-main (2)/MyPetsCR-main/Interfaz/Imagenes/fondo.jpg").scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)))
        self.setPalette(palette)
    
    def open_gmail(self):
        self.open_mail("veterinariaMiPet@gmail.com")

    def open_outlook(self):
        self.open_mail("veterinariasMiPet@outlook.com")
    
    def open_mail(self, email):
        mailto_url = QUrl(f"mailto:{email}")
        if not QDesktopServices.openUrl(mailto_url):
            QMessageBox.warning(self, "Advertencia", "No hay un programa de correo instalado.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    contact_window = ContactWindow()
    contact_window.show()
    sys.exit(app.exec())



