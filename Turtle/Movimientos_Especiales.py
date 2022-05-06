import turtle

screen = turtle.Screen()
objeto = turtle.Turtle()

objeto.speed(10) #1 al 10 lento -> rápido
objeto.circle(25)
#objeto.dot(30) #Genera un punto negro

objeto.hideturtle()
objeto.circle(150)
objeto.showturtle()
objeto.circle(350)


objeto.setx(100) #Estas coordenas se mantienen

turtle.done()