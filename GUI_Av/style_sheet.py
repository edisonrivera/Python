from ast import arg
from os import environ
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget



from sys import argv, exit
from fix_deprecated import suppress_qt_warnings


def create_app():
    aplicacion = QApplication (argv)
    ventana = QWidget()
    layout = QVBoxLayout()
    ventana.setWindowTitle("Aplicacion en PyQt5")
    aplicacion.setStyleSheet("QPushButton {margin : 20px;}")
    layout.addWidget(QPushButton("Hola Mundo"))
    ventana.setLayout(layout)
    ventana.show()
    exit(aplicacion.exec())


if __name__ == "__main__":
    suppress_qt_warnings()
    create_app()