def altura (x):
    i = niveles = 0
    while x >= 0:
        x -= i +1
        i += 1
        niveles += 1
    print ("-> ALTURA: ",niveles-1)

bloques = int(input("-> BLOQUES: "))
altura (bloques)