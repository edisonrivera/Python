import math


def square_areas_difference(radius_circle: float) -> float:
    area_cuadrado_mayor = math.pow((radius_circle*2),2)

    """
        La diferencia entre cuadrados siempre es la mitad 
        del valor del cuadrado mayor

        Formula Area Cuadrado Menor:
        area = (radius_circle**2)*2
    """
     
    return area_cuadrado_mayor / 2
     
if __name__ == "__main__":
    while True:
        try:
            radius_circle = float(input("-> Radio: "))
            diferencia_areas = square_areas_difference(radius_circle)
            print("Diferencia de",diferencia_areas, "u²")
            break
        except ValueError:
            print("Dato inválido")