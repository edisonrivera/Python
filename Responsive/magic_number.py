from random import randint

class Adivinar():
    def __init__(self,max=100,min=0):
        self.max = max
        self.min = min
        self.intentos = 0
        self.random = randint(self.min,self.max)

    def conseguir_numero(self):
        while True:
            try:
                numero_usuario = int(input(f"-> Ingrese un número entre {self.min} - {self.max}: "))
                if self.min <= numero_usuario <= self.max:
                    return numero_usuario
                else:
                    print("{:>55}".format("!!! El número no está entre 0 y 100 :("))
            except:
                print("{:>45}".format("!!! Dato no válido !!!"))
            print(end="\n")       

    def juego(self):
        while True:
            self.intentos += 1
            numero = self.conseguir_numero()
            if numero > self.random:
                print("{:>45}".format("El número ingresado es muy alto"))
            elif numero < self.random:
                print("{:>45}".format("El número ingresado en muy bajo"))
            else:
                print(end="\n")
                print("{:>60}".format("¡¡¡¡¡" + "Adivinó el número".center(25," ") + "¡¡¡¡¡"))
                print("| RESUMEN DEL JUEGO", f"| Intentos: {self.intentos} | Número a encontrar: {self.random} | Número ingresado: {numero} |")
                break
            print(end="\n")


if __name__ == "__main__":
    partida = Adivinar()
    partida.juego()