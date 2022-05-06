lista = "disco duro 500Gb;200;25;15;memoria ram 16Gb;500;30;20;ratón inalámbrico;800;12;10;tarjeta wifi;150;20;12"
sub_lista = []
o = 1
caracteristicas = {} 
list_directa = lista.split(";")
print(list_directa)
for i in range (0,16,4):
    while o <= 3:
        sub_lista.append(list_directa[i+o])
        o += 1
    o = 1
    print(sub_lista)
    caracteristicas[list_directa[i]] = sub_lista
    
print(caracteristicas)
#print ("Producto","\t\tCantidad,Precio,Descuento")
#for key,value in caracteristicas.items():
#    print(f"-> {key}" , f"{value}")