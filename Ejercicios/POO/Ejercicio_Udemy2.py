class Potencia:
    def __init__(self,base,exponente):
        self.base = base
        self.exponente = exponente
    
    def potencia(self):
        return "El resultado es", pow(self.base,self.exponente)

base = int(input("EXPONENTE: "))
exponente = int(input("BASE: "))
ejercicio = Potencia(abs(base), abs(exponente))
print (ejercicio.potencia())