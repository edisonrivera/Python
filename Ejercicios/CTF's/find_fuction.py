def comprobar(word,verse):
    band = True
    c = 0
    word = word.lower()
    verse = verse.lower()
    while band and c < len(word):
        for i in word:
            if verse.find(i) == -1:
                band = False
                break
            else:
                c += 1
    print("Si" if band else "No")

x = input("1) PALABRA: ")
y = input("2) FRASE: ")
comprobar(x,y)