esquema_edificio = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 0],
                    [1, 1, 1, 1]]

alturas_edificios = [0,0,0,0]
var_edificio = 1

def contar_altura(piso_edificio):
    for num_piso in range(len(piso_edificio)):
        if (piso_edificio[num_piso] == var_edificio):
            alturas_edificios[num_piso] += 1

def leer_pisos(edificios):
    for piso in edificios:
        if (var_edificio in piso):
            contar_altura(piso)

if __name__ == "__main__":
    leer_pisos(esquema_edificio)
    print(max(alturas_edificios))