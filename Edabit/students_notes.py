def return_max_note(diccionario: dict) -> dict:
    lista_notas = diccionario["notes"]
    max_nota = max(lista_notas)
    del(diccionario["notes"])
    diccionario["max_note"] = max_nota
    return diccionario

if __name__ == "__main__":
    diccionario = { "name": "John", "notes": [3, 5, 4] }
    diccionario_maximos = return_max_note(diccionario)
    print(diccionario_maximos)