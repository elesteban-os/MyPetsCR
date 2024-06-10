from ventanas.NewExpe import ExpedienteDialog


class Mascota:
    def __init__(self, nombre, especie, edad, alergias, padecimientos):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.alergias = alergias
        self.padecimientos = padecimientos
        

class RegistroMascotas:
    def __init__(self):
        self.mascotas = {}
        self.expedientes = {}

    def registrar_mascota(self, nombre, especie, edad, alergias, padecimientos):
        if nombre in self.mascotas:
            print(f"La mascota {nombre} ya está registrada.")
        else:
            nueva_mascota = Mascota(nombre, especie, edad, alergias, padecimientos)
            self.mascotas[nombre] = nueva_mascota
            self.expedientes[nombre] = ExpedienteDialog(nueva_mascota)
            print(f"La mascota {nombre} ha sido registrada exitosamente.")

    def agregar_entrada_expediente(self, nombre, entrada):
        if nombre in self.expedientes:
            self.expedientes[nombre].agregar_entrada(entrada)
            print(f"Entrada agregada al expediente de {nombre}.")
        else:
            print(f"No se encontró el expediente de {nombre}.")

    def mostrar_expedientes(self):
        for expediente in self.expedientes.values():
            expediente.mostrar_expediente()