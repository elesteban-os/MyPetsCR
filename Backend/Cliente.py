class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.mascotas = []
        
class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        
def mostrar_cliente_y_mascotas(cliente):
    print("Cliente:", cliente.nombre)
    print("Teléfono:", cliente.telefono)
    print("Correo:", cliente.correo)
    print("Mascotas:")
    for mascota in cliente.mascotas:
        print("- Nombre:", mascota.nombre)
        print("  Especie:", mascota.especie)
        print("  Raza:", mascota.raza)
        print("  Edad:", mascota.edad)

# Creación del cliente
cliente1 = Cliente("Vale", "123456789", "Vale@gmail.com")

# Agrega mascotas al cliente
cliente1.mascotas.append(Mascota("Chloe", "Perro", "Poodle", 3))
cliente1.mascotas.append(Mascota("Peri", "Perico", "Lora", 5))

#Probar el codigo con la información asociada a x cliente 
mostrar_cliente_y_mascotas(cliente1)