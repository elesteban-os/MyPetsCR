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
        self.conn.commit()

    def close(self):
        self.conn.close()
