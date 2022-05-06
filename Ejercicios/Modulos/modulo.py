def is_primo(x):
    __contador = 0
    for i in range (1,x+1):
        if (x%i == 0):
            __contador +=1
    print (f"{x} es PRIMO" if __contador == 2 else f"{x} no es PRIMO")