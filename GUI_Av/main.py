from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
import sys
from os import environ

# ! Arreglar el problema "deprecated"
def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


def create_app():
    app = QApplication(sys.argv)

    app.setStyle('Fusion') # ? Cambia el estilo de la pantalla
    """
        TODO Existen estos estilos: 'Fusion', 'Windows', 'WindowsVista'
    """

    root = QWidget() # ? Creamos la ventana
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Presionalo")) # ? Agregamos herramientas
    layout.addWidget(QPushButton("Holaaa")) # ? al layout ya creado

    root.setLayout(layout)
    root.show()
    sys.exit(app.exec())



if __name__ == "__main__":
    suppress_qt_warnings()
    create_app()





