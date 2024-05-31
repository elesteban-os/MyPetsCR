import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('veterinaria.db')
cursor = conn.cursor()

# Tabla de productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        codigo TEXT PRIMARY KEY,
        descripcion TEXT NOT NULL,
        marca TEXT NOT NULL,
        precio REAL NOT NULL,
        iva INTEGER NOT NULL,
        cantidad_disponible INTEGER NOT NULL,
        categoria TEXT NOT NULL
    )
''')

# Lista de productos a insertar
productos = [
    {
        "Código": "PROD001",
        "Descripción": "Alimento húmedo para gatos, sabor atún, 500 g",
        "Marca": "Kong",
        "Precio": 35.24,
        "IVA": 13,
        "CantidadDisponible": 13,
        "Categoría": "Juguetes"
    },
    
]

# Insertar productos en la tabla
for producto in productos:
    try:
        cursor.execute('''
            INSERT INTO productos (codigo, descripcion, marca, precio, iva, cantidad_disponible, categoria)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            producto["Código"],
            producto["Descripción"],
            producto["Marca"],
            producto["Precio"],
            producto["IVA"],
            producto["CantidadDisponible"],
            producto["Categoría"]
        ))
    except sqlite3.IntegrityError as e:
        print(f"Error: El producto con código {producto['Código']} ya existe en la base de datos.")

# Consulta para obtener todos los productos
cursor.execute('SELECT * FROM productos')
productos = cursor.fetchall()

# Mostrar los productos
for producto in productos:
    print(producto)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
