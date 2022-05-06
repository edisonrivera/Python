def n_grama():
    palabra = input("-> Palabra: ")
    while True:
        try:
            n = int(input("-> Numero: "))
            break
        except ValueError:
            print("Solo se permite valores enteros")
    if len(palabra) == n:
        print("-> n-grama: ", palabra)
    elif len(palabra) < n:
        print("No es posible realizar en n-grama")
    else:
        acu = mostrar = ""
        i = 0
        print("-> n-grama:", end=" ")        
        while not acu.endswith(palabra[len(palabra)-n:]):
            mostrar = palabra[i:n]
            print(mostrar, end=" ")
            acu = mostrar
            i += 1
            n += 1 

n_grama()