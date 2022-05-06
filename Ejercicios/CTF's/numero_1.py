def dates_to_evalue():
    print("{:>53}".format("Conocer cantidad de numero pares e impares en un rango establecido"))
    while True:
        try:
            inicio = int(input("-> Valor inicial: "))
            final = int(input("-> Valor final: "))
        except:
            print ("Dato erroneo")
        else:
            break
    return inicio,final

def count_numbers_even_odd(start, end):
    count_even = count_odd = 0 
    for i in range (start,end):
        if i%2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

start , end = dates_to_evalue()
count_numbers_even_odd(start, end)
print ("Pares:", count_numbers_even_odd(start, end)[0], "\tImpares:", count_numbers_even_odd(start, end)[1])