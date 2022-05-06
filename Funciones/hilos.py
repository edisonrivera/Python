import threading #Módulo de hilos

#Hilos recibirá un valor entero como argumento
class Hilos(threading.Thread):
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self) #Se inicia el contructor
    def run (self): #Se presenta un mensaje más amigable al usuario
        print("Hilo:",str(self.__x))

for i in range(10): 
    Hilos(i).start() #start() inicia la actividad de un hilo