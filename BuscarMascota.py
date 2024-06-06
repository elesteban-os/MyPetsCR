import sqlite3
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QApplication, QMainWindow
from PyQt6 import uic
import sys

class BuscarMascota(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("BuscarMascota.ui", self)
        self.pushButtonBuscar.clicked.connect(self.buscar_mascotas)

    def buscar_mascotas(self):
        nombre_mascota = self.lineEditNombreMascota.text().strip()
        nombre_dueno = self.lineEditNombreDueno.text().strip()
        especie = self.lineEditEspecie.text().strip()
        
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        
        query = '''
            SELECT mascotas.id, mascotas.nombre, mascotas.especie, mascotas.raza, mascotas.edad, clientes.nombre, clientes.apellido
            FROM mascotas
            JOIN clientes ON mascotas.id_cliente = clientes.id
            WHERE mascotas.nombre LIKE ? AND clientes.nombre LIKE ? AND mascotas.especie LIKE ?
        '''
        
        cursor.execute(query, (f'%{nombre_mascota}%', f'%{nombre_dueno}%', f'%{especie}%'))
        resultados = cursor.fetchall()
        conn.close()
        
        self.tableWidgetResultados.setRowCount(len(resultados))
        self.tableWidgetResultados.setColumnCount(7)
        self.tableWidgetResultados.setHorizontalHeaderLabels(['ID', 'Nombre', 'Especie', 'Raza', 'Edad', 'Nombre Dueño', 'Apellido Dueño'])
        
        for row_index, row_data in enumerate(resultados):
            for col_index, col_data in enumerate(row_data):
                self.tableWidgetResultados.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("VentanaPrincipal.ui", self)
        self.pushButtonBuscarMascota.clicked.connect(self.abrir_buscar_mascota)

    def abrir_buscar_mascota(self):
        self.buscar_mascota = BuscarMascota(self)
        self.buscar_mascota.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())