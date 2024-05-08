class Cita:
    def __init__(self, fecha, hora, cliente, mascota, motivo):
        self.fecha = fecha
        self.hora = hora
        self.cliente = cliente
        self.mascota = mascota
        self.motivo = motivo

def programar_cita(fecha, hora, cliente, mascota, motivo):
    cita = Cita(fecha, hora, cliente, mascota, motivo)
    # Agregar la cita a la lista de citas programadas
    citas_programadas.append(cita)
