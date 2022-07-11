import math


def cantidad_soluciones(a: float, b: float, c: float):
    n_soluciones = 0
    formula = pow(b,2) - 4*a*c
    if (formula > 0): n_soluciones = 2
    elif (formula == 0): n_soluciones = 1
    else:n_soluciones = 0
    print(f"La ecuacion tiene {n_soluciones} posibles")
    return n_soluciones

def formula_general(a: float,b: float,c: float,signo: int):
    try:
        formula = (b * -1 + (signo*math.sqrt(pow(b,2)-(4*a*c))))/(2*a)
        return formula
    except:
        return -1
    
def soluciones_cuadraticas(cant_soluciones: int, var_a: float, var_b: float,var_c: float):
    valor_x = formula_general(var_a, var_b, var_c, 1)
    valor_y = formula_general(var_a, var_b, var_c, -1)   
    if (cant_soluciones == 2):
        print(f"Soluciones    x:[{valor_x}] --- y:[{valor_y}]")
    elif (cant_soluciones == 1):
        print(f"Solucion      x:[{valor_x}]")

def solicitar_datos():
    while True:
        try:
            a = float(input("-> Valor de A: "))
            b = float(input("-> Valor de B: "))
            c = float(input("-> Valor de C: "))
            break
        except ValueError:
            print("Introduzca datos validos")
    return a,b,c

if __name__ == "__main__":
    var_a, var_b, var_c = solicitar_datos()
    n_soluciones = cantidad_soluciones(var_a,var_b,var_c)
    soluciones_cuadraticas(n_soluciones,var_a,var_b,var_c)