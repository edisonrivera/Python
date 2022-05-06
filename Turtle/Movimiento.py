import turtle
import time
screen = turtle.Screen()
objeto = turtle.Turtle()

#Grafica un CUADRADO
objeto.backward(100) #Genera línea de 100px
time.sleep(1)
objeto.right(90)
time.sleep(1)
objeto.forward(100)
time.sleep(1)
objeto.left(90)
time.sleep(1)
objeto.forward(100)
time.sleep(1)
objeto.left(90)
time.sleep(1)
objeto.forward(100)

turtle.done()