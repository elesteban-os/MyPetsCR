import sqlite3

def crear_tablas():
    # Conectar a la base de datos
    conn = sqlite3.connect('veterinaria.db')
    cursor = conn.cursor()

    # Eliminar las tablas existentes para recrearlas correctamente
    cursor.execute('DROP TABLE IF EXISTS personas')
    cursor.execute('DROP TABLE IF EXISTS clientes')
    cursor.execute('DROP TABLE IF EXISTS mascotas')
    cursor.execute('DROP TABLE IF EXISTS citas')

    # Crear tabla de personas Veterinarios y Administradores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            tipo_usuario TEXT NOT NULL,
            email TEXT,
            telefono TEXT,
            direccion TEXT,
            contrasena TEXT 
        )
    ''')

    # Crear tabla de personas Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            tipo_usuario TEXT NOT NULL,  
            email TEXT,
            telefono TEXT,
            direccion TEXT,
            contrasena TEXT, 
            mascota TEXT 
        )
    ''')

    # Crear tabla de mascotas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            raza TEXT NOT NULL,
            edad INTEGER NOT NULL,
            id_cliente INTEGER NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes (id)
        )
    ''')

    # Crear tabla de citas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS citas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            id_cliente INTEGER NOT NULL,
            id_mascota INTEGER NOT NULL,
            id_veterinario INTEGER NOT NULL,
            descripcion TEXT NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes (id),
            FOREIGN KEY (id_mascota) REFERENCES mascotas (id),
            FOREIGN KEY (id_veterinario) REFERENCES personas (id)
        )
    ''')

    # Guardar cambios
    conn.commit()

    # Depuración: Imprimir el esquema de la base de datos
    for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
        print(row)

    # Depuración: Imprimir el esquema de la tabla clientes
    for row in cursor.execute("PRAGMA table_info(clientes);"):
        print(row)

    # Cerrar conexión
    conn.close()

# Crear las tablas
crear_tablas()
    # Guardar cambios y cerrar conexión
    conn.commit()
    conn.close()

# Crear las tablas
crear_tablas()
