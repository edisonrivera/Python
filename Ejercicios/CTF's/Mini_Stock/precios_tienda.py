def rellenar_lista():
    stock = {}
    print("Para detener ingresar \"stop\" en el espacio \"-> Fruta a stock: \"")
    while True:
        nombre_producto = input("-> Fruta a stock: ")
        if nombre_producto == "stop":
            break
        else: 
            valor_producto = float(input(f"-> Precio de {nombre_producto} (c/kg): "))
            stock[f"{nombre_producto}"] = valor_producto
    return stock

def facturar (**lista_frutas):
    total = 0
    contador = 1
    factura = open(r"C:\Users\pc\Python\Ejercicios\CTF's\Mini_Stock\factura.txt", "w")
    factura.write("------------------------------------------------------\n")
    factura.write("|" + "-- FRUTAS --".center(20," ") + "|" + "-- KILOS --".center(15," ") + "|" + "-- PRECIO --".center(15," ") + "|\n")
    factura.write("------------------------------------------------------\n")
    print("|" + "Realizar venta".center(25," ") + "|")
    print("Para detener ingresar \"stop\" en el espacio \"-> Fruta: \"")
    while True:
        nombre_a_validar = input("-> Fruta: ")
        if nombre_a_validar in lista_frutas:
            kilos = float(input(f"-> Kilos de {nombre_a_validar}: "))
            subtotal_unitario = kilos*lista_frutas[nombre_a_validar]
            factura.write(f"| {contador}" + f"{nombre_a_validar}".center(18," ") + "|" + f"{kilos}".center(15," ") + "|" + f"{subtotal_unitario}".center(15," ") + "|\n")
            total += subtotal_unitario
            contador += 1
        elif nombre_a_validar == "stop":
            break
        else:
            print("! Fruta no encontrada en el stock ¡")
    iva = round(total * 0.12,2)
    total += iva 
    factura.write("------------------------------------------------------\n")
    factura.write(" " + " ".center(19) + " " + "|" + "- I.V.A -".center(14, " ") + "|" + "|" + f"{iva}".center(15, " ") + "|\n")
    factura.write(" " + " ".center(19) + " " + "|" + "- TOTAL -".center(14, " ") + "|" + "|" + f"{total}".center(15, " ") + "|\n")
    factura.write(" " + " ".center(19) + " " + "---------------------------------\n\n")
    factura.write("{:>40}".format("Gracias por su compra !!!"))
    factura.close()

dictionary = rellenar_lista()
facturar(**dictionary)