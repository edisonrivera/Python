def palindromo(frase):
    new_frase = ""
    c = len(frase) - 1
    band = True
    for i in frase:
        i = str(i)
        i = i.lower()
        new_frase += i
    for i in new_frase:
        if i.isspace():
            c-=1
            continue
        elif (i != new_frase[c]):
            band = False
            print(new_frase[c],"-",i)
            break
        c -= 1
    print("Es palindromo" if band else "No es palindromo")

x = input("-> FRASE: ")
palindromo(x)