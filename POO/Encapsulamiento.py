class encapsulamiento:
    def __init__(self):
        self.__privado_attrib = "Hola mundo"

    def __privado_met(self):
        print("What")

    def publico_attrib(self):
        return print(self.__privado_attrib)
    
    def public_met (self):
        return self.__privado_met()
e = encapsulamiento()
e.publico_attrib()
e.public_met()