from math import floor


def shift_to_right(numero: int, veces: int):
    CONSTANTE = 2
    operacion_final = floor(numero/(CONSTANTE**veces));
    return operacion_final

if __name__ == "__main__":
    numero = int(input("-> Numero: "))
    veces = int(input("-> Veces: "))
    operacion_final = shift_to_right(numero, veces)
    print("Valor final ->",operacion_final)