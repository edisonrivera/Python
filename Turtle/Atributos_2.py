import turtle
#Ventana
screen = turtle.Screen()
objeto = turtle.Turtle()
screen.bgcolor("black")

#Objeto
objeto.shape("turtle") #Nombres Predeterminados
objeto.begin_fill() #Rellenar
objeto.color("green")
objeto.circle(50)
objeto.end_fill() #Terminar rellenado

#LEVANTAR EL LAPIZ
objeto.sety(-150)
objeto.penup() #Hace que no se escriba el rastro
objeto.circle(150)

#BAJAR EL LAPIZ
objeto.pendown() #Vuelve a escribir el rastro
objeto.circle(150)
objeto.undo() #Deshace el último rastro

#DEJAR UN RASTRO
objeto.forward(100)
objeto.stamp() #Dejar una marca de la figura
objeto.forward(100)

#REINICIAR
objeto.reset() #Limpia el lienzo por completo
    
turtle.done()