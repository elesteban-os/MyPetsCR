from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
from PyQt6 import QtWidgets, uic
from datetime import datetime
import sqlite3

# Clase para gestionar las sedes y sus horarios disponibles
class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios_disponibles = set()

    def agregar_horario_disponible(self, fecha_hora):
        self.horarios_disponibles.add(fecha_hora)

    def bloquear_horario(self, fecha_hora):
        if fecha_hora in self.horarios_disponibles:
            self.horarios_disponibles.remove(fecha_hora)

# Clase para la gestión de la base de datos SQLite
class Database:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insertar_cita(self, fecha, id_cliente, id_mascota, id_veterinario, descripcion):
        try:
            self.cursor.execute('''
                INSERT INTO citas (fecha, id_cliente, id_mascota, id_veterinario, descripcion) VALUES 
                (?, ?, ?, ?, ?)
            ''', (fecha, id_cliente, id_mascota, id_veterinario, descripcion))
            self.conn.commit()
            print("Cita insertada correctamente en la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al insertar cita: {e}")

    def close(self):
        self.conn.close()

# Clase principal de la aplicación PyQt6
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Citas_Client.ui', self)

        self.sedes = [
            Sede('Central'),
            Sede('Norte'),
            Sede('Sur'),
            Sede('Este'),
            Sede('Oeste')
        ]

        for sede in self.sedes:
            self.sede.addItem(sede.nombre)

        self.pushButton_2.clicked.connect(self.enviar_confirmacion)
        self.pushButton.clicked.connect(self.salir)

    def crear_cita(self, cliente, fecha_hora, sede):
        if fecha_hora in sede.horarios_disponibles:
            cita = {
                'cliente': cliente,
                'fecha_hora': fecha_hora,
                'sede': sede
            }
            sede.bloquear_horario(fecha_hora)
            self.enviar_confirmacion(cliente, cita)
            return cita
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Horario no disponible.")
            return None

    def enviar_confirmacion(self, cliente, cita):
        destinatario = cliente['correo']
        asunto = "Confirmación de cita"
        mensaje = f"Estimado {cliente['nombre']},\n\nSu cita ha sido confirmada para el {cita['fecha_hora']} en la sede {cita['sede'].nombre}.\n\nSaludos,\nAdministrador"

        remitente = "valeriabadilla2004@gmail.com"
        password = os.getenv("Password")

        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 465)
            server.starttls()
            server.login(remitente, password)
            server.send_message(msg)
            server.quit()
            print(f"Correo enviado a {destinatario}")
            QtWidgets.QMessageBox.information(self, "Confirmación", "Cita creada y confirmada con éxito.")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
            QtWidgets.QMessageBox.warning(self, "Error", f"Error al enviar correo: {e}")

    def salir(self):
        self.close()

    def enviar_confirmacion(self):
        cliente = {
            'nombre': self.nombrecliente.text(),
            'correo': self.correo.text()
        }
        fecha_hora = datetime.combine(self.dateTimeEdit.date().toPyDate(), self.dateTimeEdit.time().toPyTime())
        
        sede_nombre = self.sede.currentText()
        sede = next((s for s in self.sedes if s.nombre == sede_nombre), None)
        
        if sede:
            cita = self.crear_cita(cliente, fecha_hora, sede)
            if cita:
                # Puedes realizar otras acciones aquí si es necesario
                pass
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Sede no encontrada o horario no disponible.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())