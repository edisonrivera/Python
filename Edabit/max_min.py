def return_max_min(number_user : str) -> int:
    max_number = sorted(number_user, reverse=True)
    min_number = sorted(number_user)
    max_number = "".join(max_number)
    min_number = "".join(min_number)
    return  int(max_number) - int(min_number)

if __name__ == "__main__":
    number_str = input("- Numero: ")
    if (number_str.isdigit()):
        valor_final = return_max_min(number_str)
        print("La resta es:",valor_final)