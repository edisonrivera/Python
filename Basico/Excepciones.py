while(True):
    try:
        variable = float(input("Intoduce un numero flotante: "))
        print ("Bien hecho")
    except:
        print ("Ingresaste cualquier cosa")
    else:
        print ("Eres un duro")
        break
    finally: #Se ejecuta independiente del caso en el que hay entrado
        print ("Terminando de iniciar...")


num = 1

assert num != 1, "Hola"