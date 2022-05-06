import readchar
from os import system
direction = readchar.readchar().decode

if direction == "w":
    print ("You push \'w\' key")
else:
    print ("Hello")
    system("cls")