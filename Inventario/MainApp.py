from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QPushButton, QHBoxLayout
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación Principal")
        self.setGeometry(100, 100, 300, 200)

        # Llamamos al login al iniciar la aplicación
        self.ventana_login = VentanaLogin(self)
        self.ventana_login.show()

    def mostrar_vista(self, vista):
        """Simula el cambio de vista de la aplicación"""
        if vista == "menu_principal":
            self.setWindowTitle("Menú Principal")
            self.setGeometry(100, 100, 300, 200)
            # Aquí puedes añadir widgets o vistas del menú principal
class VentanaMenu(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Referencia a la aplicación principal
        self.setWindowTitle("Menu Principal")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Ejemplo de un label para el menú
        self.label = QLabel("Bienvenido al Menú Principal perro")
        layout.addWidget(self.label)

        # Aquí puedes agregar más elementos según el menú que desees

        self.setLayout(layout)
class VentanaLogin(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app  # Referencia a la ventana principal
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # Etiqueta Usuario
        self.label_usuario = QLabel("Usuario:")
        layout.addWidget(self.label_usuario)

        # Caja de texto para Usuario
        self.input_usuario = QLineEdit()
        self.input_usuario.setPlaceholderText("Ingrese su usuario")
        layout.addWidget(self.input_usuario)

        # Etiqueta contrasena
        self.label_contrasena = QLabel("Contraseña:")
        layout.addWidget(self.label_contrasena)

        # Layout horizontal para la contrasena + botón de mostrar
        contrasena_layout = QHBoxLayout()
        self.input_contrasena = QLineEdit()
        self.input_contrasena.setPlaceholderText("Ingrese su contraseña")
        self.input_contrasena.setEchoMode(QLineEdit.Password)  # Cambié EchoMode a Password
        contrasena_layout.addWidget(self.input_contrasena)

        # Botón para mostrar/ocultar contrasena
        self.boton_mostrar = QPushButton("👁")
        self.boton_mostrar.setFixedWidth(30)  # Tamaño pequeño
        self.boton_mostrar.setCheckable(True)
        self.boton_mostrar.clicked.connect(self.toggle_contrasena)
        contrasena_layout.addWidget(self.boton_mostrar)

        layout.addLayout(contrasena_layout)

        # Botón de login
        self.boton_login = QPushButton("Iniciar Sesión")
        self.boton_login.clicked.connect(self.verificar_login)
        layout.addWidget(self.boton_login)

        self.setLayout(layout)

    def toggle_contrasena(self):
        """Muestra u oculta la contrasena"""
        if self.boton_mostrar.isChecked():
            self.input_contrasena.setEchoMode(QLineEdit.Normal)  # Cambié EchoMode a Normal
        else:
            self.input_contrasena.setEchoMode(QLineEdit.Password)  # Cambié EchoMode a Password

    def verificar_login(self):
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()

        if self.verificar_credenciales(usuario, contrasena):  # Verificar contra base de datos
            self.main_app.mostrar_vista("menu_principal")  # Cambiar a la vista del menú
            self.close()  # Cierra la ventana de login
            # Crear e inicializar la nueva ventana
            self.ventana_menu = VentanaMenu(self.main_app)
            self.ventana_menu.show()  # Mostrar la ventana del menú
            
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def verificar_credenciales(self, usuario, contrasena):
        """Simulación de validación de usuario y contrasena"""
        # Aquí puedes agregar la lógica para validar el usuario contra una base de datos
        return usuario == "admin" and contrasena == "1234"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()  # Instanciamos la aplicación principal
    sys.exit(app.exec_())
