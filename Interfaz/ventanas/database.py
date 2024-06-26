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
                apellido TEXT,
                tipo_usuario TEXT,
                email TEXT,
                telefono TEXT,
                direccion TEXT,
                contrasena TEXT,
                mascota TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mascotas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                id_cliente INTEGER,
                alergias TEXT,
                padecimientos TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                tipo_usuario TEXT,
                email TEXT,
                telefono TEXT,
                direccion TEXT,
                contrasena TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                id_cliente INTEGER,
                id_mascota INTEGER,
                id_veterinario INTEGER,
                descripcion TEXT,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id),
                FOREIGN KEY (id_mascota) REFERENCES mascotas(id),
                FOREIGN KEY (id_veterinario) REFERENCES personas(id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expedientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_mascota INTEGER,
                nombre TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                alergias TEXT,
                padecimientos TEXT,
                historial TEXT,
                FOREIGN KEY (id_mascota) REFERENCES mascotas(id)
            )
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = Database()
    db.close()

class InsertarBaseDatos:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insertar_datos_iniciales(self):
        try:
            # Insertar un cliente
            self.cursor.execute('''
                INSERT INTO clientes (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena, mascota) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)
            ''', ('Juan', 'Perez', 'Cliente', 'juan.perez@example.com', '123456789', 'Calle 123', 'password123', 'Bobby'))

            # Obtener el ID del cliente insertado
            id_cliente = self.cursor.lastrowid

            # Insertar una mascota asociada al cliente
            self.cursor.execute('''
                INSERT INTO mascotas (nombre, especie, raza, edad, id_cliente, alergias, padecimientos) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', ('Bobby', 'Perro', 'Labrador', 5, id_cliente, 'None', 'None'))

            # Obtener el ID de la mascota insertada
            id_mascota = self.cursor.lastrowid

            # Insertar un veterinario
            self.cursor.execute('''
                INSERT INTO personas (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', ('Valerin', 'Calderon', 'veterinario', 'vale.calderon@gmail.com', '987654321', 'Avenida 456', 'vetpassword'))

            # Insertar un Administrador
            self.cursor.execute('''
                INSERT INTO personas (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', ('Meibel', 'Mora', 'Administrador', 'meimb03@gmail.com', '987654321', 'Cartago', '1234'))

            # Obtener el ID del veterinario insertado
            id_veterinario = self.cursor.lastrowid

            # Insertar una cita
            self.cursor.execute('''
                INSERT INTO citas (fecha, id_cliente, id_mascota, id_veterinario, descripcion) VALUES 
                (?, ?, ?, ?, ?)
            ''', ('2024-05-15 10:00', id_cliente, id_mascota, id_veterinario, 'Consulta general'))

            # Guardar cambios
            self.conn.commit()
            print("Datos iniciales insertados y conexión cerrada.")

        except sqlite3.Error as e:
            print(f"Error al insertar datos: {e}")
        finally:
            self.conn.close()

if __name__ == "__main__":
    insercion = InsertarBaseDatos()
    insercion.insertar_datos_iniciales()

def insertar_expediente_de_prueba():
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()
    
    # Insertar un expediente ejemplo
    cursor.execute('''
        INSERT INTO expedientes (id_mascota, nombre, especie, raza, edad, alergias, padecimientos, historial)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (1, 'Puchi', 'Canino', 'Labrador', 1, 'Polvo', 'Tos seca', 'Historial de prueba'))
    
    conn.commit()
    conn.close()
    print("Expediente de prueba insertado.")

if __name__ == "__main__":
    insertar_expediente_de_prueba()
