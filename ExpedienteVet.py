from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic
import sqlite3
import sys

class ExpedienteDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Datos1_Proyecto1/MyPetsCR/Interfaz/ExpedienteVet.ui", self)

        self.id_expediente = None  # Inicializar id_expediente
        self.pushButton.clicked.connect(self.guardar_cambios)
        self.pushButtonMostrarDatos.clicked.connect(self.cargar_datos)
        self.pushButton_2.clicked.connect(self.close)  # Botón Cancelar
        self.pushButton_3.clicked.connect(self.buscar_expediente)

    def buscar_expediente(self):
        nombre_buscar = self.lineEdit_8.text().strip()
        if not nombre_buscar:
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre para buscar.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expedientes WHERE nombre=?", (nombre_buscar,))
        expediente = cursor.fetchone()
        conn.close()

        if expediente:
            self.id_expediente = expediente[0]
            self.cargar_datos()
        else:
            QMessageBox.warning(self, "Error", "Expediente no encontrado.")

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
                self.lineEdit_7.setText(str(expediente[8]))  # Historial
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

        if not (nombre and especie and raza and edad.isdigit() and alergias and padecimientos and nuevo_registro):
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos correctamente.")
            return

        if self.id_expediente is None:
            QMessageBox.warning(self, "Error", "No se ha seleccionado ningún expediente.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT historial FROM expedientes WHERE id=?", (self.id_expediente,))
            historial = cursor.fetchone()[0]
            if historial:
                historial += "\n" + nuevo_registro
            else:
                historial = nuevo_registro

            cursor.execute('''
                UPDATE expedientes
                SET nombre=?, especie=?, raza=?, edad=?, alergias=?, padecimientos=?, historial=?
                WHERE id=?
            ''', (nombre, especie, raza, int(edad), alergias, padecimientos, historial, self.id_expediente))
            conn.commit()
            QMessageBox.information(self, "Éxito", "Datos actualizados correctamente en el expediente.")
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Error al actualizar datos en el expediente: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    expediente_dialog = ExpedienteDialog()
    expediente_dialog.show()
    sys.exit(app.exec())
