from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from PyQt6 import uic
import sqlite3
import sys

class HistorialDialog(QDialog):
    def __init__(self, id_expediente, parent=None):
        super().__init__(parent)
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\HistorialVet.ui", self)
        self.id_expediente = id_expediente
        self.pushButton.clicked.connect(self.guardar_historial)
        self.pushButton_2.clicked.connect(self.close)  # Botón Cancelar
        self.cargar_historial()

    def cargar_historial(self):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT historial FROM expedientes WHERE id=?", (self.id_expediente,))
        historial = cursor.fetchone()
        conn.close()

        if historial and historial[0]:
            rows = historial[0].split('\n')
            self.tableWidget.setRowCount(len(rows))
            for row_num, row_data in enumerate(rows):
                columns = row_data.split('|')
                for column_num, column_data in enumerate(columns):
                    self.tableWidget.setItem(row_num, column_num, QTableWidgetItem(column_data.strip()))

    def guardar_historial(self):
        rows = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                row_data.append(item.text() if item else '')
            rows.append('|'.join(row_data))

        historial = '\n'.join(rows)
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE expedientes
            SET historial=?
            WHERE id=?
        ''', (historial, self.id_expediente))
        conn.commit()
        conn.close()
        self.accept()

class ExpedienteDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:\Datos1_Proyecto1\MyPetsCR\Interfaz\ExpedienteVet.ui", self)

        self.id_expediente = None
        self.id_mascota = None
        self.pushButton.clicked.connect(self.guardar_cambios)
        self.pushButtonMostrarDatos.clicked.connect(self.mostrar_historial)
        self.pushButton_2.clicked.connect(self.close)  # Botón Cancelar
        self.pushButton_3.clicked.connect(self.buscar_expediente)

    def buscar_expediente(self):
        nombre_buscar = self.lineEdit_8.text().strip()
        if not nombre_buscar:
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre para buscar.")
            return

        print(f"Buscando mascota con nombre: {nombre_buscar}")

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        
        # Primero, buscar la mascota en la tabla 'mascotas'
        cursor.execute("SELECT id FROM mascotas WHERE nombre=?", (nombre_buscar,))
        mascota = cursor.fetchone()
        
        if mascota:
            self.id_mascota = mascota[0]
            print(f"Mascota encontrada: ID {self.id_mascota}")
            
            # Ahora, buscar el expediente usando el id_mascota en la tabla 'expedientes'
            cursor.execute("SELECT * FROM expedientes WHERE id_mascota=?", (self.id_mascota,))
            expediente = cursor.fetchone()
            conn.close()

            if expediente:
                print(f"Expediente encontrado: {expediente}")
                self.id_expediente = expediente[0]
                self.cargar_datos()
            else:
                print("Expediente no encontrado")
                QMessageBox.warning(self, "Error", f"Expediente no encontrado para la mascota: {nombre_buscar}")
        else:
            conn.close()
            print("Mascota no encontrada")
            QMessageBox.warning(self, "Error", f"Mascota no encontrada: {nombre_buscar}")

    def cargar_datos(self):
        if self.id_expediente is None:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún expediente.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expedientes WHERE id=?", (self.id_expediente,))
        expediente = cursor.fetchone()
        conn.close()

        if expediente:
            try:
                self.lineEdit.setText(str(expediente[2]))  # Nombre de la mascota
                self.lineEdit_3.setText(str(expediente[3]))  # Especie
                self.lineEdit_5.setText(str(expediente[4]))  # Raza
                self.lineEdit_4.setText(str(expediente[5]))  # Edad
                self.lineEdit_2.setText(str(expediente[6]))  # Alergias
                self.lineEdit_6.setText(str(expediente[7]))  # Padecimientos
                self.lineEdit_7.clear()  # Limpiar el historial para edición
            except IndexError:
                QMessageBox.warning(self, "Error", "La estructura de la base de datos no es la esperada.")
        else:
            self.lineEdit.setText("Expediente no encontrado")

    def guardar_cambios(self):
        nombre = self.lineEdit.text().strip()
        especie = self.lineEdit_3.text().strip()
        raza = self.lineEdit_5.text().strip()
        edad = self.lineEdit_4.text().strip()
        alergias = self.lineEdit_2.text().strip()
        padecimientos = self.lineEdit_6.text().strip()
        nuevo_registro = self.lineEdit_7.text().strip()

        if not (nombre and especie and raza and edad.isdigit() and alergias and padecimientos):
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos correctamente.")
            return

        if self.id_expediente is None:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún expediente.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE expedientes
                SET nombre=?, especie=?, raza=?, edad=?, alergias=?, padecimientos=?, historial=?
                WHERE id=?
            ''', (nombre, especie, raza, int(edad), alergias, padecimientos, nuevo_registro, self.id_expediente))
            conn.commit()
            QMessageBox.information(self, "Éxito", "Datos actualizados correctamente en el expediente.")
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Error al actualizar datos en el expediente: {e}")
        finally:
            conn.close()

    def mostrar_historial(self):
        historial_dialog = HistorialDialog(self.id_expediente, self)
        historial_dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    expediente_dialog = ExpedienteDialog()
    expediente_dialog.show()
    sys.exit(app.exec())




    