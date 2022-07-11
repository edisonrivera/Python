dictionary = {"Nombre" : ["Estela", "Edison", "Carlos", "Juan"],
              "Sueldo" : [700, 650, 500, 500]}

if __name__ == "__main__":
    print("{Nombre[0]} gana {Sueldo[0]} mensualemente".format_map(dictionary))