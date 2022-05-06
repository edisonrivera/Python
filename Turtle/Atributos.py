import turtle

screen = turtle.Screen()
objeto = turtle.Turtle()

#Ventana
screen.title("PROYECTO DE PRUEBA")
screen.bgcolor("black")

#Tortuga
objeto.color("green", "blue") #Borde y relleno, Color del rastro
objeto.fillcolor("white") #Relleno
objeto.shapesize(3,3,2) #Ancho Largo Border
objeto.pensize(3)
objeto.forward(250)

turtle.textinput("Iniciando...", "Nombre primer tortuga: ")

turtle.done()