import sqlite3

class Database:
    def __init__(self, db_name="veterinaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        # Verificar si la tabla clientes_old existe
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clientes_old'")
        if self.cursor.fetchone() is None:
            # Renombrar la tabla clientes original si existe
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clientes'")
            if self.cursor.fetchone() is not None:
                self.cursor.execute("ALTER TABLE clientes RENAME TO clientes_old")

        # Crear la tabla clientes nueva con las columnas correctas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                telefono TEXT,                           
                direccion TEXT,
                tipo_usuario TEXT,
                email TEXT,
                contrasena TEXT
            )
        ''')

        # Transferir los datos relevantes de clientes_old a la nueva tabla clientes
        self.cursor.execute('''
            INSERT INTO clientes (id, nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena)
            SELECT id, nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena
            FROM clientes_old
        ''')

        # Eliminar la tabla clientes_old si ya no es necesaria
        self.cursor.execute('DROP TABLE IF EXISTS clientes_old')

        # Crear la tabla mascotas con las columnas correctas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mascotas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                alergias TEXT,
                padecimientos TEXT,  
                id_cliente INTEGER,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
            )
        ''')

        # Crear la tabla personas con las columnas correctas
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
            CREATE TABLE IF NOT EXISTS expedientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_mascota INTEGER,
                nombre TEXT,
                especie TEXT,
                raza TEXT,
                edad INTEGER,
                alergias TEXT,
                padecimientos TEXT,
                FOREIGN KEY (id_mascota) REFERENCES mascotas(id)
            )
        ''')
        self.conn.commit()

    def close(self):
        self.conn.close()

# Crear la base de datos y las tablas
db = Database()

# Cerrar la conexión a la base de datos
db.close()
