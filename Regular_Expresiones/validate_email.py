import re


"""
    TODO re.search(pattern, string, flags = 0 (optional))
    
    ! ---- Flags -----
    ? re.IGNORECASE -> Insensitive
    ? re.MULTILINE -> Mas de una linea
    ? re.DOTALL -> Hasta un punto. 

    
    ! ---- Basics -----
    ? . -> Cualquier caracter excepto una nueva linea.
    ? * -> 0 o mas repeticiones.
    ? + -> 1 o mas repeticiones.
    ? ? -> 0 o 1 repeticion.
    ? {m} -> m repeticiones.
    ? {m,n} -> m-n repeticiones.
    ? [^char] -> Excepto el char.
    ? (...) -> Capturar un grupo.
    ? (?:...) -> No capturar un grupo. Al usar group(n) no toma en
    ? cuenta ese grupo para el conteo
    
    
    ! ---- Especials -----
    ? \w -> Alfanumericos.
    ? \W -> NO alfanumericos.
    ? \d -> digitos decimales.
    ? \D -> NO digitos decimales.
    ? \s -> espacios en blanco.
    ? \S -> NO espacios en blanco.
    ? | -> or.
"""

if __name__ == "__main__":
    email = input("Email: ").strip()

    if (re.search("^(\w+\.?){1,2}@(\w+\.){1,2}(com|edu|es|org|ec)$", email, re.IGNORECASE)):
        print("Validado")
    else:
        print("No valido")

