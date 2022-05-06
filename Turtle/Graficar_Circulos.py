#Modulos
import turtle
from random import choice
#Atributos de la ventana
screen = turtle.Screen()
screen.title("LIENZO DE PRUEBA")
screen.bgcolor("black")

#Variables:
colores = ["green","blue","white","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
first_controler = second_controler = " "
#Atributos del objeto
objeto = turtle.Turtle()
objeto.speed(10)
objeto.pensize(3)
objeto.shape("turtle")
objeto.shapesize(1,1,1)

#Acciones
for i in range (1,7):
    first_controler = choice(colores)
    objeto.penup()
    objeto.color(first_controler)
    objeto.fillcolor(colores[2])
    while first_controler == second_controler:
        objeto.color(first_controler)
    objeto.sety(-25 - 25*i)
    objeto.pendown()
    objeto.circle(25 + 25 *i)
    second_controler = first_controler
    
turtle.done()