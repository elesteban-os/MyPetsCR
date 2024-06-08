import sqlite3
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6 import uic

class BuscarCliente(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("BuscarCliente.ui", self)
        self.pushButton.clicked.connect(self.buscar_cliente)
        self.tableWidget.cellDoubleClicked.connect(self.seleccionar_cliente)

    def buscar_cliente(self):
        criterio = self.lineEdit.text().strip()
        if not criterio:
            return
        
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nombre, apellido, tipo_usuario, email, telefono, direccion, mascota FROM clientes 
            WHERE nombre LIKE ? OR apellido LIKE ? OR email LIKE ?
        ''', (f'%{criterio}%', f'%{criterio}%', f'%{criterio}%'))
        resultados = cursor.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(resultados))
        self.tableWidget.setColumnCount(8)  # Ajustar el número de columnas
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido', 'Tipo de Usuario', 'Email', 'Teléfono', 'Dirección', 'Mascota'])
        
        for row_index, row_data in enumerate(resultados):
            for col_index, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def seleccionar_cliente(self, row, column):
        cliente_id = self.tableWidget.item(row, 0).text()
        self.parent().lineEdit_12.setText(cliente_id)
        self.accept()