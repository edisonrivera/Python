class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1  #Se tiene que tener en cuenta el variable
        else:           #a la que se accede
            self.b = 1

objetoEjemplo = ClaseEjemplo(4)
print("A -> ",objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'): #Definir si es un atributo
    print("B ->", objetoEjemplo.b)