#
# DECORATORS
#

class CreatePj():
    number_of_pj = 0 # No está instanciada con "self" así que es global y constante para todos los objetos creados

    def __init__(self,namepj):
        self.namepj = namepj
        CreatePj.add_pj() # Llamado para añadir en 1 
    
    @classmethod
    def number_of_pjs(cls): # Muestra el número de personajes totales existentes
        return cls.number_of_pj

    @classmethod
    def add_pj(cls): # Añade en 1 al numero de personajes creados
        cls.number_of_pj += 1


pj_one = CreatePj("Estela")
pj_two = CreatePj("Paul")
print("-> Pj's:",CreatePj.number_of_pjs()) # Llama a la función que muestra el número de personajes creados