import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox, QAbstractItemView

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox, QAbstractItemView

class PaymentSystem(QWidget):
    def __init__(self, items):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Sistema de Pagos')
        self.setGeometry(100, 100, 400, 300)
        
        # Crear widgets
        self.name_label = QLabel('Nombre del Cliente:')
        self.name_input = QLineEdit()
        
        self.items_label = QLabel('Selecciona los Artículos:')
        self.items_list = QListWidget()
        self.items_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        
        for item, price in items.items():
            list_item = QListWidgetItem(f'{item} - ${price:.2f}')
            list_item.setData(1, price)
            self.items_list.addItem(list_item)
        
        self.pay_button = QPushButton('Procesar Pago')
        self.pay_button.clicked.connect(self.process_payment)
        
        # Configurar layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.items_label)
        layout.addWidget(self.items_list)
        layout.addWidget(self.pay_button)
        
        self.setLayout(layout)
    
    def process_payment(self):
        name = self.name_input.text()
        selected_items = self.items_list.selectedItems()
        
        if not name or not selected_items:
            QMessageBox.warning(self, 'Error', 'Por favor, complete todos los campos y seleccione al menos un artículo')
            return
        
        total_amount = sum(item.data(1) for item in selected_items)
        
        # Aquí podrías agregar la lógica para procesar el pago (por ejemplo, conectarte a una API de pagos)
        
        QMessageBox.information(self, 'Pago Procesado', f'El pago de ${total_amount:.2f} de {name} ha sido procesado exitosamente')

if __name__ == '__main__':
    items = {
        'Artículo 1': 10.00,
        'Artículo 2': 20.00,
        'Artículo 3': 15.50,
        'Artículo 4': 5.75,
        'Artículo 5': 30.00
    }
    
    app = QApplication(sys.argv)
    payment_system = PaymentSystem(items)
    payment_system.show()
    sys.exit(app.exec())


