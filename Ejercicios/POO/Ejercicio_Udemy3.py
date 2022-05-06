class Calculadora:
    def __init__(self):
        self.firts_number = int(input("-> PRIMER VALOR: "))
        self.second_number = int(input("-> SEGUNDO VALOR: "))

    def suma (self):
        print("SUMA: ",self.firts_number + self.second_number)
    
    def resta (self):
        print("RESTA:", self.firts_number - self.second_number)
       
    def multiplicacion (self):
        print ("MULTIPLICACION:",self.firts_number * self.second_number)
    
    def division (self):
        try:
            print("DIVISION: ", self.firts_number / self.second_number)
        except ZeroDivisionError:
            return "MATH ERROR"

calculos = Calculadora()
calculos.suma()
calculos.resta()
calculos.multiplicacion()
calculos.division()