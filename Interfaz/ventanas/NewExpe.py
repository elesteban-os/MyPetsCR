from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt6 import uic
import sqlite3
import sys

class ExpedienteDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Datos1_Proyecto1\MyPetsCR\Interfaz\NewExpediente.ui", self)

        self.pushButton.clicked.connect(self.guardar_cambios)
        self.pushButtonMostrarDatos.clicked.connect(self.cargar_datos)
        self.pushButton_2.clicked.connect(self.close)  # Botón Cancelar
        self.pushButton_3.clicked.connect(self.buscar_mascota)

        # Hacer que las casillas de texto no sean editables
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8.setReadOnly(False)

    def buscar_mascota(self):
        nombre_buscar = self.lineEdit_8.text().strip()
        if not nombre_buscar:
            QMessageBox.warning(self, "Error", "Por favor ingrese un nombre para buscar.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mascotas WHERE nombre=?", (nombre_buscar,))
        mascota = cursor.fetchone()
        conn.close()

        if mascota:
            self.id_mascota = mascota[0]
            # Llenar las casillas con los datos de la mascota
            self.lineEdit.setText(str(mascota[1]))  # Nombre
            self.lineEdit_3.setText(str(mascota[2]))  # Especie
            self.lineEdit_5.setText(str(mascota[3]))  # Raza
            self.lineEdit_4.setText(str(mascota[4]))  # Edad
            self.lineEdit_2.setText(str(mascota[6]))  # Alergias
            self.lineEdit_6.setText(str(mascota[7]))  # Padecimientos
        else:
            QMessageBox.warning(self, "Error", "Mascota no encontrada.")
    
    def cargar_datos(self):
        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM mascotas WHERE id=?", (self.id_mascota,))
        mascota = cursor.fetchone()
        conn.close()

        if mascota:
            try:
                self.lineEdit.setText(str(mascota[1]))  # Nombre
                self.lineEdit_3.setText(str(mascota[2]))  # Especie
                self.lineEdit_5.setText(str(mascota[3]))  # Raza
                self.lineEdit_4.setText(str(mascota[4]))  # Edad
                self.lineEdit_2.setText(str(mascota[6]))  # Alergias
                self.lineEdit_6.setText(str(mascota[7]))  # Padecimientos
            except IndexError:
                QMessageBox.warning(self, "Error", "La estructura de la base de datos no es la esperada.")
        else:
            self.lineEdit.setText("Mascota no encontrada")

    def guardar_cambios(self):
        nombre = self.lineEdit.text().strip()
        especie = self.lineEdit_3.text().strip()
        raza = self.lineEdit_5.text().strip()
        edad = self.lineEdit_4.text().strip()
        alergias = self.lineEdit_2.text().strip()
        padecimientos = self.lineEdit_6.text().strip()

        if not (nombre and especie and edad.isdigit()):
            QMessageBox.warning(self, "Error", "Por favor complete todos los campos correctamente.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE expedientes
                SET nombre=?, especie=?, raza=?, edad=?, alergias=?, padecimientos=?
                WHERE id_mascota=?
            ''', (nombre, especie, raza, int(edad), alergias, padecimientos, self.id_mascota))
            conn.commit()
            QMessageBox.information(self, "Éxito", "Expediente creado correctamente.")
        except sqlite3.Error as e:
            QMessageBox.warning(self, "Error", f"Error al crear el expediente: {e}")
        finally:
            conn.close()
    def agregar_entrada(self):
        nueva_entrada = self.lineEditNuevaEntrada.text().strip()
        if not nueva_entrada:
            QMessageBox.warning(self, "Error", "Por favor ingrese una entrada válida.")
            return

        conn = sqlite3.connect('veterinaria.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expedientes (id_mascota, entrada)
            VALUES (?, ?)
        ''', (self.id_mascota, nueva_entrada))
        conn.commit()
        conn.close()

        QMessageBox.information(self, "Éxito", "Entrada agregada correctamente.")
        self.lineEditNuevaEntrada.clear()
        self.cargar_datos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    expediente_dialog = ExpedienteDialog()
    expediente_dialog.show()
    sys.exit(app.exec())
    