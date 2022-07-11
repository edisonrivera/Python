def forma(valores: list,fuction):
    for i in valores:         
        print(f'f({i}) = {fuction(i)}')

forma([x for x in range (0,11)],lambda o : o**2 -4*o +2)