nombre = "Hola mundo"
codigo = "linea de codigo"
forma = "El {} es generalmente la {}".format(nombre,codigo)
print (forma)
forma = "El {1} es generalmente la {0}".format(nombre,codigo)
print (forma)
#Para poder centrar
print ('{:>35}'.format('Titulo centrado'))