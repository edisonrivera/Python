from random import randint

class Adivinar():
    def __init__(self,max=100,min=0):
        self.max = max
        self.min = min
        self.random = randint(0,100)

    def conseguir_numero(self):
        numero_usuario = input(f"-> Ingrese un número entre {self.min} - {self.max}: ")
        condicion = self.evaluar_numero_usuario(numero_usuario)
        if condicion:
            return int(numero_usuario)
        else:
            self.conseguir_numero()
         
    def evaluar_numero_usuario(self,numero_evaluar):
        if int(numero_evaluar):
            return self.min <= int(numero_evaluar) <= self.max
        else:
            return False

    def juego(self):
        intentos = 0
        while True:
            numero_usuario = self.conseguir_numero()
            if numero_usuario > self.random:
                print("El número ingresado es muy alto")
                intentos += 1
            elif numero_usuario < self.random:
                print("El número ingresado en muy bajo")
                intentos += 1
            else:
                print("¡¡¡¡¡" + "Adivinó el número".center(25," ") + "¡¡¡¡¡")
                print("| RESUMEN DEL JUEGO |", f"| Intentos: {intentos} | Numero a encontrar: {self.random} | Numero ingresado: {numero_usuario} |")
                break
    
partida = Adivinar()
partida.juego()