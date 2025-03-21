from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QWidget
import sys

class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba de botón Show/Ocultar")
        self.resize(300, 150)

        layout = QVBoxLayout()

        # Caja de texto para contraseña
        self.input_contraseña = QLineEdit()
        self.input_contraseña.setPlaceholderText("Ingrese su contraseña")
        self.input_contraseña.setEchoMode(QLineEdit.Password)  # Ocultar texto
        layout.addWidget(self.input_contraseña)

        # Layout horizontal para el botón de mostrar/ocultar
        hbox = QHBoxLayout()
        self.boton_mostrar = QPushButton("👁")  # Prueba con "👁" o con "Show"
        self.boton_mostrar.setFixedWidth(50)
        self.boton_mostrar.setCheckable(True)
        self.boton_mostrar.clicked.connect(self.toggle_contrasena)  # Cambié el nombre de la función
        hbox.addWidget(self.boton_mostrar)
        layout.addLayout(hbox)

        self.setLayout(layout)

    def toggle_contrasena(self):  # Cambié el nombre aquí también
        if self.boton_mostrar.isChecked():
            self.input_contraseña.setEchoMode(QLineEdit.Normal)
        else:
            self.input_contraseña.setEchoMode(QLineEdit.Password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec_())
