import turtle
from time import sleep
from random import randint

mover = 0.1
marcador = 0
maximo = 0

root = turtle.Screen()
root.title("Juego de la culebra")
root.bgcolor("black")
root.setup(650,650)

snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()

snake.direction = "stop"

comida = turtle.Turtle()
comida.shape("triangle")
comida.color("red")
comida.penup()
comida.goto(randint(-300,300),randint(-300,300))
comida.speed(0)

snake_body = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,280)
texto.write("Marcador: 0 \t Puntuación Máxima: 0",align="center", font=("verdana",20,"normal"))


def arriba():
    snake.direction = 'up'

def abajo():
    snake.direction = 'down'

def derecha():
    snake.direction = 'right'

def izquierda():
    snake.direction = 'left'

def movimiento():
    if snake.direction == 'up':
        arriba = snake.ycor()
        snake.sety(arriba + 20)

    if snake.direction == 'down':
        abajo = snake.ycor()
        snake.sety(abajo - 20)
        
    if snake.direction == 'right':
        derecha = snake.xcor()
        snake.setx(derecha + 20) 

    if snake.direction == 'left':
        izquierda = snake.xcor()
        snake.setx(izquierda - 20)
        
root.listen()
root.onkeypress(arriba,"Up")
root.onkeypress(abajo,"Down")
root.onkeypress(derecha,"Right")
root.onkeypress(izquierda,"Left")

while True:
    root.update()
    if snake.xcor() > 300 or snake.xcor() < -300 or  snake.ycor() > 300 or snake.ycor() < -300:
        sleep(2)
        for i in snake_body:
            i.clear()
            i.hideturtle()

        snake.home()
        snake.direction = "stop"
        snake_body.clear()
        marcador = 0
        texto.clear()
        texto.write(f"Marcador {marcador} \t Puntuación Máxima {maximo}",align="center",font=("verdana",20,"normal"))

    if snake.distance(comida) < 20:
        x = randint(-250,250)
        y = randint(-250,250)
        comida.goto(x,y) 
        agregar_al_cuerpo = turtle.Turtle()
        agregar_al_cuerpo.shape("square")
        agregar_al_cuerpo.color("green")
        agregar_al_cuerpo.penup()
        agregar_al_cuerpo.goto(0,0)
        agregar_al_cuerpo.speed(0)
        snake_body.append(agregar_al_cuerpo)
        marcador += 10
        if marcador > maximo:
            maximo = marcador
            texto.clear()
            texto.write(f"Marcador {marcador} \t Puntuación Máxima {maximo}",align="center",font=("verdana",20,"normal"))

    total = len(snake_body)
    for i in range (total-1,0,-1):
        x = snake_body[i-1].xcor()
        y = snake_body[i-1].ycor()
        snake_body[i].goto(x,y)

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        snake_body[0].goto(x,y)

    movimiento()

    for i in snake_body:
        if i.distance(snake) < 20:
            for i in snake_body:
                i.clear()
                i.hideturtle()
            snake.home()
            snake_body.clear()
        marcador = 0
        texto.clear()
        texto.write(f"Marcador {marcador} \t Puntuación Máxima {maximo}",align="center",font=("verdana",20,"normal"))
    sleep(mover)

turtle.done()