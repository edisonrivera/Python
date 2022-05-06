from PyQt5.QtWidgets import QApplication, QLabel,QPushButton,QVBoxLayout, QWidget,QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import sys

def root():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Use PyQt5")
    window.setFixedWidth(1000)
    window.move(500,400)
    window.setStyleSheet("background: #011;")

    grid = QGridLayout()
    
    image = QPixmap(r"GUI\PyQt5\logo.png")
    logo = QLabel()
    logo.setPixmap(image)
    
    logo.setStyleSheet("margin-top: 25px;")

    grid.addWidget(logo,0,3)

    window.setLayout(grid)

    window.show() 
    sys.exit(app.exec())

root()