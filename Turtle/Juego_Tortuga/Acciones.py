import turtle
from random import randint
class Screen():
    def __init__(self):
        self.screen = turtle.Screen()
        
    def attrs (self):
        self.screen.title("{:>100}".format("RACING TURTLE GAME"))
        self.screen.bgcolor("black")
        self.screen.setup(650,350)

class Player():
    def __init__(self):
        self.player = turtle.Turtle()
        self.player.shape("turtle")
        self.__i = 0

    def attrs_player(self, color):
        self.player.color(color)
        self.player.pensize(2)
    
    def move_player(self, posicion):
        self.player.penup()
        self.__i = 1 if posicion == "up" else -1
        self.player.goto(300,100*self.__i)
        self.player.pendown()
        self.player.right(90)
        self.player.forward(50)
        self.player.backward(100)
        self.player.forward(50)
        self.player.penup()
        self.player.setx(-290)
        self.player.left(90)
        self.player.pendown()

    def avanzar(self,avanzar):
        self.player.forward(avanzar*20)

class Settings():
    def __init__(self):
        self.name_turtle = turtle.textinput("Iniciando...", "Nombre de la tortuga: ")
    def __str__(self):
        return self.name_turtle

class Game():
    def __init__(self,name_one,name_second):
        self.name_one = name_one
        self.name_second = name_second
        self.random_number = randint(1,7)
        
    def calcular (self,controler):
        if controler % 2 == 0:
            self.user_number = turtle.numinput(self.name_one,"Range (1 - 6):",minval=1,maxval=6)
        else:
            self.user_number = turtle.numinput(self.name_second,"Range (1 - 6):",minval=1,maxval=6)

        if self.user_number == self.random_number:
            return self.user_number
        else:
            return 0