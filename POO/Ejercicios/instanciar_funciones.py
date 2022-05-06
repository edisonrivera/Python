from datetime import datetime


# def externa(nombre: str):
#     def interna():
#         print(f"Hola {nombre}")

#     return interna

# instancia = externa("Juanito")
# instancia()

def fecha ():
    print(datetime.today().strftime("%d-%m-%Y")) #Mostrar fecha actual

def hora ():
    print(datetime.now().strftime("%H-%M-%S")) # Mostrar hora actual

def externa(foreing_fuction):
    def interna():
        print("-> Esta es la ejecución de la función interna <-")
        foreing_fuction()
        print("-> End of foreing_fuction <-")
    return interna

mostrar_hora = externa(hora)
mostrar_hora()