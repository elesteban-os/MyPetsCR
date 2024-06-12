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

        # Comprobar si las columnas existen antes de intentar agregarlas
        self.agregar_columna_si_no_existe('mascotas', 'alergias', 'TEXT')
        self.agregar_columna_si_no_existe('mascotas', 'padecimientos', 'TEXT')

        self.conn.commit()

    def agregar_columna_si_no_existe(self, table_name, column_name, column_type):
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col[1] for col in self.cursor.fetchall()]
        if column_name not in columns:
            self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")

    def close(self):
        self.conn.close()


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
            
            self.cursor.execute('''
                INSERT INTO clientes (nombre, apellido, tipo_usuario, email, telefono, direccion, contrasena, mascota) VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?)
            ''', ('Fabiola', 'Castro', 'Cliente', 'fmelendez@gmail.com', '65788967', 'Calle 126', '456', 'Alex'))  

            # Obtener el ID del cliente insertado
            id_cliente = self.cursor.lastrowid

            # Insertar una mascota asociada al cliente
            self.cursor.execute('''
                INSERT INTO mascotas (nombre, especie, raza, edad, id_cliente) VALUES 
                (?, ?, ?, ?, ?)
            ''', ('Bobby', 'Perro', 'Labrador', 5, id_cliente))

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

# Uso de las clases para crear tablas e insertar datos
if __name__ == "__main__":
    # Crear la base de datos y sus tablas
    db = Database()
    db.close()

    # Insertar datos iniciales
    insercion = InsertarBaseDatos()
    insercion.insertar_datos_iniciales()



