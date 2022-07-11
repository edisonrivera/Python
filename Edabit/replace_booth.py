texto = "AEAEAEAR"

cifra = {"A": "E", "E": "A"}

texto_cifrado = "".join(cifra.get(letra, letra) for letra in texto)
print(texto_cifrado)