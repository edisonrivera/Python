from random import randrange
import time
contador = 0
while contador < 10:
    n = randrange(1000)
    time.sleep (2)
    contador += 1
    print (f"{contador}", ".- ",n)