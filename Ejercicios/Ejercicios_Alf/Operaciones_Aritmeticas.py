def modo_uso():
    print("Para terminar la ejecución ingrese la palabra \'salir\'")
    print("Operadores: ", "[+] [-] [*] [/] [** potencia]")

def calcular ():
    expresion = " "
    while expresion != "salir":
        expresion = input("Expresion: ")
        print("-> Salida: ", eval(expresion))


calcular()