from re import split


def parse_code(cadena: str) -> dict:
    first_name, second_name, id = split("0+", cadena)
    datos = {"firts_name" : first_name, 
            "second_name" : second_name,
            "id" : id}

    return datos

    
if __name__ == "__main__":
    datos_dict = parse_code("John000Doe000123")
    for key, value in datos_dict.items():
        print(key,"->",value)