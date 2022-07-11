from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("C:\\Users\\pc\\Cursos_de_Programacion\\Python\\Qt\\main_window.ui", self)
        self.agregar_boton.clicked.connect(self.on_agregar_boton_clicked)

    def on_agregar_boton_clicked(self):
        nombre = self.nombre_lineedit.text()
        edad = int(self.edad_lieedit.text())
        correo = self.correo_lieedit.text()
        if (nombre == ""):
            QMessageBox.critical(self, "Nombre vacio")
        if (edad == ""):
            QMessageBox.critical(self, "Edad vacia")
        if (correo == ""):
            QMessageBox.critical(self, "Correo vacio")

        edad = int(edad)

        q = QSqlQuery()
        if (q.prepare("INSERT INTO site (sitio, password) VALUES (nombre, correo)")):
            q.addBindValue(nombre)
            q.addBindValue(correo)
            if (q.exec()):
                if(QMessageBox.question(self, "Borrar?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes):
                    self.nombre_lineedit.clear()
                    self.edad_lieedit.clear()
                    self.correo_lieedit.clear()