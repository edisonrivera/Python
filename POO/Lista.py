class Inventario:
    all = []
    def __init__(self,nombre,cantidad,precio : float):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def __repr__(self):
        return f"Item: {self.nombre}, {self.cantidad}, {self.precio}"

item = Inventario("Laptop",2,100.5)
itemDos = Inventario("Mouse",10,8)
itemTres = Inventario("Teclado",2,50)
print(Inventario.all)