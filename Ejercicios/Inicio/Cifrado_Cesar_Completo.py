def cifrar_cesar(cadena,desplazado):
    encriptado = '' 
    for letra in cadena:
        letra = str(letra) 
        if not letra.isalpha():
            encriptado += letra
            continue
        letra = ord(letra)
        numchr = letra + desplazado
        if letra >= 65 and letra <=90:
            if numchr > 90:
                letra = numchr - 26 
            else: 
                letra = numchr       
        if letra >= 97 and letra <= 122:
            if numchr > 122:
                letra = numchr - 26 
            else:
                letra = numchr         
        encriptado += chr(letra) 
    print(encriptado)

cadena = input("-> A ENCRIPTAR: ")
while True:
    desplazar = int(input("-> DESPLAZAR EN: "))
    if desplazar >= 1 and desplazar <= 25:
        break
cifrar_cesar(cadena,desplazar)