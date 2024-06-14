import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Se omite la creación de tablas para mantener el foco en las citas y expedientes
        pass

    def close(self):
        self.conn.close()

class SistemaCitas:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def obtener_citas_pendientes(self):
        try:
            self.cursor.execute("SELECT * FROM citas")
            citas = self.cursor.fetchall()
            return citas
        except sqlite3.Error as e:
            print(f"Error al obtener citas: {e}")
            return []

    def enviar_recordatorio(self, cita_id):
        try:
            self.cursor.execute("SELECT * FROM citas WHERE id=?", (cita_id,))
            cita = self.cursor.fetchone()
            if cita:
                id_cliente = cita[2]
                fecha = cita[1]
                detalles = f"Fecha: {fecha}\nDescripción: {cita[5]}"
                # Aquí simularíamos el envío de un recordatorio, por ejemplo, a través de una API de notificaciones o correo electrónico
                print(f"Recordatorio enviado para la cita ID {cita_id}:\n{detalles}")
            else:
                print(f"No se encontró la cita con ID {cita_id}")
        except sqlite3.Error as e:
            print(f"Error al obtener cita para enviar recordatorio: {e}")

    def cancelar_cita(self, cita_id):
        try:
            self.cursor.execute("DELETE FROM citas WHERE id=?", (cita_id,))
            self.conn.commit()
            print(f"Cita con ID {cita_id} cancelada correctamente.")
        except sqlite3.Error as e:
            print(f"Error al cancelar cita: {e}")

    def close(self):
        self.conn.close()

def insertar_expediente_de_prueba():
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    
    # Insertar un expediente ejemplo
    cursor.execute('''
        INSERT INTO expedientes (id_mascota, nombre, especie, raza, edad, alergias, padecimientos, historial)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (19, 'Puchi', 'Canino', 'Felino', 1, 'Polvo', 'Tos seca', 'Historial de prueba'))
    
    conn.commit()
    conn.close()
    print("Expediente de prueba insertado.")

if __name__ == "__main__":
    db = Database()
    sistema_citas = SistemaCitas()

    # Lógica para enviar recordatorios de citas
    citas_pendientes = sistema_citas.obtener_citas_pendientes()
    for cita in citas_pendientes:
        cita_id = cita[0]
        sistema_citas.enviar_recordatorio(cita_id)

    # Simulación de cancelación de una cita
    cita_id_a_cancelar = 1  # ID de la cita a cancelar (simulado)
    sistema_citas.cancelar_cita(cita_id_a_cancelar)

    db.close()
    sistema_citas.close()
