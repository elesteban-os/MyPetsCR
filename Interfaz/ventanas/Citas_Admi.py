from PyQt6 import QtWidgets, uic
from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

class Database:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                id_cliente INTEGER,
                sede TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            )
        ''')

        self.conn.commit()

    def insertar_cliente(self, nombre, email):
        self.cursor.execute('''
            INSERT INTO clientes (nombre, email) VALUES (?, ?)
        ''', (nombre, email))
        self.conn.commit()
        return self.cursor.lastrowid

    def obtener_cliente_id(self, email):
        self.cursor.execute('SELECT id FROM clientes WHERE email = ?', (email,))
        cliente = self.cursor.fetchone()
        return cliente[0] if cliente else None

    def insertar_cita(self, fecha, id_cliente, sede):
        self.cursor.execute('''
            INSERT INTO citas (fecha, id_cliente, sede) VALUES (?, ?, ?)
        ''', (fecha, id_cliente, sede))
        self.conn.commit()

    def close(self):
        self.conn.close()


    def agregar_columna_si_no_existe(self, table_name, column_name, column_type):
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in self.cursor.fetchall()]
        if column_name not in columns:
            self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")

    def insertar_cita(self, cliente_id, fecha_hora, sede_nombre):
        try:
            self.cursor.execute('''
                INSERT INTO citas (fecha, id_cliente, id_mascota, id_veterinario, descripcion) 
                VALUES (?, ?, ?, ?, ?)
            ''', (fecha_hora, cliente_id, 1, 1, 'Consulta general'))  # Ajusta los valores según sea necesario
            self.conn.commit()
            print("Cita insertada en la base de datos.")
        except sqlite3.Error as e:
            print(f"Error al insertar la cita: {e}")

    def obtener_cliente_id(self, email):
        self.cursor.execute('SELECT id FROM clientes WHERE email = ?', (email,))
        cliente = self.cursor.fetchone()
        return cliente[0] if cliente else None

    def close(self):
        self.conn.close()

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

    def crear_cita(self, cliente, fecha_hora, sede, db):
        if fecha_hora in sede.horarios_disponibles:
            cita = Cita(cliente, fecha_hora, sede)
            self.citas.append(cita)
            sede.bloquear_horario(fecha_hora)
            self.enviar_confirmacion(cliente, cita)
            cliente_id = db.obtener_cliente_id(cliente['correo'])
            db.insertar_cita(cliente_id, fecha_hora, sede.nombre)
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
        uic.loadUi('Citas_Admi.ui', self)

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

    def enviar_confirmacion(self):
        cliente = {
            'nombre': self.nombrecliente.text(),
            'correo': self.Correo.text()
        }
        fecha_hora = datetime.combine(self.dateTimeEdit.date().toPyDate(), self.dateTimeEdit.time().toPyTime())
        
        sede_nombre = self.sede.currentText()
        sede = next((s for s in self.sedes if s.nombre == sede_nombre), None)
        
        if sede:
            sede.agregar_horario_disponible(fecha_hora)
            administrador = Administrador()
            db = Database()
            cita = administrador.crear_cita(cliente, fecha_hora, sede, db)
            if cita:
                QtWidgets.QMessageBox.information(self, "Confirmación", "Cita creada y confirmada con éxito.")
            db.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Sede no encontrada o horario no disponible.")

    def salir(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
