def anagrama(one,two):
    band = True
    one = one.lower()
    two = two.lower()
    for i in one:
        letter = two.count(i)
        if letter != 1:
            band = False
            break
    print("Anagramas" if band else "No son anagramas")
            
x = input("1-> CADENA: ")
y = input("2-> CADENA: ")
anagrama(x,y)