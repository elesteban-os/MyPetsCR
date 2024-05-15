import sqlite3

# Conectar a la base de datos 
conn = sqlite3.connect('veterinaria.db')
cursor = conn.cursor()

# Tabla de personas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        tipo TEXT NOT NULL,
        email TEXT,
        telefono TEXT
    )
''')

# Tabla mascotas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mascotas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especie TEXT NOT NULL,
        raza TEXT,
        edad INTEGER,
        id_cliente INTEGER,
        FOREIGN KEY(id_cliente) REFERENCES personas(id)
    )
''')

# Tabla citas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        id_cliente INTEGER,
        id_mascota INTEGER,
        id_veterinario INTEGER,
        descripcion TEXT,
        FOREIGN KEY(id_cliente) REFERENCES personas(id),
        FOREIGN KEY(id_mascota) REFERENCES mascotas(id),
        FOREIGN KEY(id_veterinario) REFERENCES personas(id)
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
