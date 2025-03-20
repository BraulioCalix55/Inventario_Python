import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QListView, QPushButton
from PyQt6.QtCore import QStringListModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Modelo import Producto  # Importar la clase Producto desde modelo.py

# Conexión con la base de datos
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Gestión de Inventario")
        self.setGeometry(100, 100, 400, 300)

        # Crear el widget principal y el layout
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        # Agregar un título
        self.titulo = QLabel("Lista de productos")
        layout.addWidget(self.titulo)

        # Crear el QListView para mostrar los productos
        self.lista_productos = QListView()
        self.model = QStringListModel()
        self.lista_productos.setModel(self.model)
        layout.addWidget(self.lista_productos)

        # Botón para cargar los productos
        self.boton_cargar = QPushButton("Cargar Productos")
        self.boton_cargar.clicked.connect(self.cargar_productos)
        layout.addWidget(self.boton_cargar)

        widget.setLayout(layout)

    def cargar_productos(self):
        # Limpiar la lista antes de cargar los productos
        self.model.setStringList([])

        # Obtener los productos de la base de datos
        session = SessionLocal()
        productos = session.query(Producto).all()

        # Crear una lista de nombres de productos
        lista_productos = [f"{producto.nombre} - {producto.categoria} (Cantidad: {producto.cantidad})" for producto in productos]
        
        # Actualizar el modelo de la lista
        self.model.setStringList(lista_productos)

        # Cerrar la sesión después de usarla
        session.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
