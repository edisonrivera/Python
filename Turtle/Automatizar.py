#Modulos
import turtle
from random import choice
from time import sleep
#Atributos de la ventana
screen = turtle.Screen()
screen.title("GRAFICAR CUADRADO")
screen.bgcolor("black")

#Variables:
colores = ["green","blue","white","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#Atributos del objeto
objeto = turtle.Turtle()
objeto.speed(10)
objeto.pensize(3)
objeto.shape("turtle")
objeto.shapesize(1,1,1)

"""
#Accion: GRAFICAR CUADRADO
for i in range (1,5):
    objeto.color(choice(colores))
    objeto.fillcolor(colores[2])
    objeto.forward(100)
    sleep(1)
    objeto.right(90)   
    sleep(1)
"""
"""
#Accion: GRAFICAR TRIANGULO
for i in range(3):
    objeto.color(choice(colores))
    objeto.fillcolor(colores[2])
    objeto.forward(300)
    objeto.left(120)
"""
"""
#Accion: Graficar Paralelogramo
for i in range(4):
    objeto.color(choice(colores))
    objeto.fillcolor(colores[2])
    objeto.forward(100)
    objeto.left(72) if i%2 == 0 else objeto.left(108)
"""
"""
#Accion: Graficar Pentágono
for i in range(5):
    objeto.color(choice(colores))
    objeto.fillcolor(colores[2])
    objeto.forward(100)
    objeto.left(72)
"""
#Accion: Graficar Rombo
for i in range(4):
    objeto.color(choice(colores))
    objeto.fillcolor(colores[2])
    objeto.right()

turtle.done()