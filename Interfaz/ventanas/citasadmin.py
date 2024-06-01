from PyQt6 import QtWidgets, uic
from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios_disponibles = set()

    def agregar_horario_disponible(self, fecha_hora):
        self.horarios_disponibles.add(fecha_hora)

    def bloquear_horario(self, fecha_hora):
        if fecha_hora in self.horarios_disponibles:
            self.horarios_disponibles.remove(fecha_hora)


class Cita:
    def __init__(self, cliente, fecha_hora, sede):
        self.cliente = cliente
        self.fecha_hora = fecha_hora
        self.sede = sede


class Administrador:
    def __init__(self):
        self.citas = []

    def crear_cita(self, cliente, fecha_hora, sede):
        if fecha_hora in sede.horarios_disponibles:
            cita = Cita(cliente, fecha_hora, sede)
            self.citas.append(cita)
            sede.bloquear_horario(fecha_hora)
            self.enviar_confirmacion(cliente, cita)
            return cita
        else:
            print("Horario no disponible")
            return None

    def enviar_confirmacion(self, cliente, cita):
        destinatario = cliente['correo']
        asunto = "Confirmación de cita"
        mensaje = f"Estimado {cliente['nombre']},\n\nSu cita ha sido confirmada para el {cita.fecha_hora} en la sede {cita.sede.nombre}.\n\nSaludos,\nAdministrador"
        enviar_correo(destinatario, asunto, mensaje)


def enviar_correo(destinatario, asunto, mensaje):
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
    except Exception as e:
        print(f"Error al enviar correo: {e}")


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        self.sedes = [
            Sede('Central'),
            Sede('Norte'),
            Sede('Sur'),
            Sede('Este'),
            Sede('Oeste')
        ]

        for sede in self.sedes:
            self.comboBox.addItem(sede.nombre)

        self.pushButton.clicked.connect(self.enviar_confirmacion)
        self.pushButton_2.clicked.connect(self.salir)

    def enviar_confirmacion(self):
        cliente = {
            'nombre': self.lineEdit.text(),
            'correo': self.lineEdit_2.text()
        }
        fecha_hora = datetime.combine(self.dateEdit.date().toPyDate(), self.timeEdit.time().toPyTime())
        
        sede_nombre = self.comboBox.currentText()
        sede = next((s for s in self.sedes if s.nombre == sede_nombre), None)
        
        if sede:
            sede.agregar_horario_disponible(fecha_hora)
            administrador = Administrador()
            administrador.crear_cita(cliente, fecha_hora, sede)
        else:
            print("Sede no encontrada")

    def salir(self):
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
