
import sqlite3

class insertarBaseDatos:
    def __init__(self):
        self.conn = sqlite3.connect('veterinaria.db')
        self.cursor = self.conn.cursor()

    def insertar_datos_iniciales(self):
        try:
            # Insertar un cliente
            self.cursor.execute('''
                INSERT INTO clientes (nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', ('Kevin', 'Chinchilla', '66441589', 'Calle 200', 'Cliente', 'kevin@gmail.com', '789'))  
           
            self.cursor.execute('''
                INSERT INTO clientes (nombre, apellido, telefono, direccion, tipo_usuario, email, contrasena) VALUES 
                (?, ?, ?, ?, ?, ?, ?)
            ''', ('Fabiola', 'Castro', '65431267', 'Calle 126', 'Cliente', 'fabi@gmail.com', '456'))  


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

            # Insertar un Adminstrador
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

# Uso de la clase para insertar datos
if __name__ == "__main__":
    insercion = insertarBaseDatos()
    insercion.insertar_datos_iniciales()
