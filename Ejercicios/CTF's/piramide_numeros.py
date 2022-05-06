def get_number ():
    while True:
        try:
            number = int(input("-> Ingrese numero: "))
            if (number > 0):
                break
            else:
                print ("Solo se admiten numero positivos")
        except:
            print ("Solo se admiten numeros")
    return number

def pyramid(number):
    if (number % 2 != 0): number += 1
    else: number -= 1
    for i in range (1,number+1,2):  
        aux = i
        print (i, end = " ")
        while aux != 1:
            aux -= 2
            print(aux, end = " ")
        print(end = "\n")

pyramid(get_number())