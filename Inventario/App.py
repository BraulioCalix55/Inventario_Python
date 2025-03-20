from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QDialog
from Modelo import Producto  # Importa la clase Producto desde modelo.py
import sys

# Crear la sesión de la base de datos
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Ventana secundaria (nueva ventana) ahora heredando de QDialog
class VentanaSecundaria(QDialog):
    def __init__(self):
        super().__init__()
        layout_principal = QVBoxLayout()
        self.setWindowTitle("Ventana Secundaria")
        self.setGeometry(400, 200, 400, 300)

        # Contenido de la ventana secundaria
        mensaje = QLabel("¡Estás en la Ventana Secundaria!")
        layout_principal.addWidget(mensaje)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Escribe algo aquí")
        layout_principal.addWidget(self.line_edit)

        # Botón para cerrar la ventana secundaria
        boton_secundario = QPushButton("Cerrar Ventana Secundaria")
        boton_secundario.clicked.connect(self.accept)
        layout_principal.addWidget(boton_secundario)

        self.setLayout(layout_principal)

# Ventana principal
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 400, 400)

        # Estilo CSS para la ventana principal
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                font-family: 'Arial';
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }

            QLabel {
                font-family: 'Arial';
                font-size: 14px;
                color: #333333;
            }

            QLineEdit {
                border: 2px solid #4CAF50;
                padding: 5px;
                border-radius: 5px;
                font-size: 14px;
            }

            QComboBox {
                font-size: 14px;
                padding: 5px;
                border: 2px solid #4CAF50;
                border-radius: 5px;
            }

            QComboBox::drop-down {
                border: none;
            }

            QComboBox QAbstractItemView {
                border: 2px solid #4CAF50;
                background-color: #ffffff;
            }
        """)

        # Layout y elementos de la ventana principal
        layout = QVBoxLayout()

        # Etiqueta
        self.label = QLabel("Bienvenido al Menú Principal")
        layout.addWidget(self.label)

        # Caja de texto
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Escribe tu nombre aquí")
        layout.addWidget(self.line_edit)

        # Crear un botón para cambiar a la ventana secundaria
        self.boton_abrir = QPushButton("Abrir Ventana Secundaria")
        self.boton_abrir.clicked.connect(self.abrir_ventana_secundaria)
        layout.addWidget(self.boton_abrir)

        # Crear un QComboBox para mostrar productos
        self.combo_box = QComboBox()
        layout.addWidget(self.combo_box)

        # Llamar a la función para cargar productos en el combo box
        self.cargar_productos_en_combo_box()

        # Establecer el layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_ventana_secundaria(self):
        ventana_secundaria = VentanaSecundaria()
        ventana_secundaria.exec()

    def cargar_productos_en_combo_box(self):
        # Obtener los productos de la base de datos
        productos = Producto.obtener_productos(session)

        # Limpiar el combo box antes de agregar los nuevos productos
        self.combo_box.clear()

        # Verificar si se han encontrado productos
        if productos:
            for producto in productos:
                self.combo_box.addItem(producto.nombre)
        else:
            print("No se encontraron productos en la base de datos.")

# Iniciar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
