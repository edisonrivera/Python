from ast import arg
from os import environ
from tkinter import Button
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget, QMessageBox



from sys import argv, exit
from fix_deprecated import suppress_qt_warnings

def boton_activo():
    alerta = QMessageBox()
    alerta.setText("Tu clickeaste el boton")
    alerta.exec()



def create_app():
    aplicacion = QApplication (argv)
    ventana = QWidget()
    layout = QVBoxLayout()
    ventana.setWindowTitle("Aplicacion en PyQt5")
    aplicacion.setStyleSheet("QPushButton {padding : 20px;}")
    boton = QPushButton("Push Me!")
    boton.clicked.connect(boton_activo)
    layout.addWidget(boton)
    ventana.setLayout(layout)
    ventana.show()
    exit(aplicacion.exec())


if __name__ == "__main__":
    suppress_qt_warnings()
    create_app()