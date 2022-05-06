def verificar(cifra): #Funcion de verificación de la cifra
    verificador = True
    for i in range(2,10):
        if (str(i) in cifra):
            verificador = False
            break
    return verificador
   
def decimal_to_binario(cifra):
    sub_acumulador = acumulador = ""
    cifra2 = cifra = int(cifra)
    while cifra != 1 and cifra != 0:
        aux = int(cifra)%2
        iterar_cifra = int(cifra // 2)
        aux = int(aux)
        sub_acumulador += str(aux)
        cifra = iterar_cifra
    else:
        sub_acumulador += str(cifra)

    acumulador = "".join(reversed(sub_acumulador)) # Revertir un objeto iterable
    print("|DECIMAL: |",f"{cifra2}","| ------>","| BINARIO: |",f"{acumulador}","|")
    
def binario_to_decimal(cifra):
    exponente = len(cifra)-1
    acumulador = 0
    for i in cifra:
        if i == str(1):
            acumulador += (2**exponente)
        exponente -= 1
    print("|BINARIO: |",f"{cifra}","| ------>","| DECIMAL: |",f"{acumulador}","|")

numero_usuario = input("-> Numero: ")
decision = verificar(numero_usuario) #Verificar en que base está
binario_to_decimal(numero_usuario) if decision else decimal_to_binario(numero_usuario)