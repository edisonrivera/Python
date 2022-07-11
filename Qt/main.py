from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import *
from main_window import MainWindow
from sys import argv, exit
from os import environ



def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


def database():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("C:\\Users\\pc\\Cursos_de_Programacion\\Python\\Passwords\\Base_Datos\\passwords.db")
    db.open()
    query = QSqlQuery()
    query.prepare("SELECT * FROM site")
    if (query.exec()):
        print("Se pudo conectar con la base de datos")
    query.result()


def main():
    app = QApplication(argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    exit(app.exec())

if __name__ == "__main__":
    suppress_qt_warnings()
    database()
    main()