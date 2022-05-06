import math 
def area_circle(radius):
    return math.pi*(math.pow(radius,2))

def volumen_circle(area,altura):
    volumen = area*altura
    print (f"--> AREA DEL CIRCULO: {area:1.5f}\n--> VOLUMEN DEL CILINDRO: {volumen:1.5f}".format(area,volumen))

radius = float(input("-> Ingrese el radio: "))
altura = float(input("-> Ingrese el altura: "))
volumen_circle(area_circle(radius),altura)