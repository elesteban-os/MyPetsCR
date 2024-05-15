import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('veterinaria.db')
cursor = conn.cursor()

# Insertar un cliente
cursor.execute('''
    INSERT INTO personas (nombre, apellido, tipo, email, telefono) VALUES 
    (?, ?, ?, ?, ?)
''', ('Juan', 'Perez', 'cliente', 'juan.perez@example.com', '123456789'))

# Insertar un veterinario
cursor.execute('''
    INSERT INTO personas (nombre, apellido, tipo, email, telefono) VALUES 
    (?, ?, ?, ?, ?)
''', ('Valerin', 'Calderon', 'veterinario', 'vale.calderon@gmail.com.com', '987654321'))

# Obtener el ID del cliente insertado
id_cliente = cursor.lastrowid

# Insertar una mascota asociada al cliente
cursor.execute('''
    INSERT INTO mascotas (nombre, especie, raza, edad, id_cliente) VALUES 
    (?, ?, ?, ?, ?)
''', ('Bobby', 'Perro', 'Labrador', 5, id_cliente))

# Obtener el ID del veterinario insertado
id_veterinario = cursor.lastrowid

# Insertar una cita
cursor.execute('''
    INSERT INTO citas (fecha, id_cliente, id_mascota, id_veterinario, descripcion) VALUES 
    (?, ?, ?, ?, ?)
''', ('2024-05-15 10:00', id_cliente, cursor.lastrowid, id_veterinario, 'Consulta general'))

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
print("Datos iniciales insertados y conexión cerrada.")