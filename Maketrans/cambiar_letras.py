"""
    TODO Esta funcion es usada para cambiar letras en una cadena de texto
    TODO al mismo tiempo.
"""

def transform_txt(to_transform: str, const_first:str, const_second:str) -> str:
    table = to_transform.maketrans(const_first, const_second)
    return to_transform.translate(table)


if __name__ == "__main__":
    text_decode = "128 895 556 788 999"
    const_first = "89"
    const_second = "98"
    text_decode = transform_txt(text_decode, const_first, const_second)
    print("Text decode:", text_decode)