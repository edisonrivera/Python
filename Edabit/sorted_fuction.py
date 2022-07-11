def order_tuple(details: list) -> list:
    sorted_details = sorted(details, key = lambda notes: (notes[1], notes[2]), reverse= True)
    return sorted_details

def order_str_num(list_mix: list) -> list:
    order_list_mix = sorted(list_mix, key= lambda number_total: int("".join([number for number in number_total if number.isdigit()])))
    return order_list_mix

def order_dict(dict_dates: dict) -> dict:
    sorted_dict = dict(sorted(dict_dates.items(), key=lambda date: date[1], reverse = True))
    return sorted_dict


if __name__ == "__main__":
    participant_list = [
        ('Alison', 50, 18),
        ('Terence', 75, 12),
        ('David', 75, 20),
        ('Jimmy', 90, 22),
        ('John', 45, 12)
    ]   

    # ? Ordenar tupla
    order_details = order_tuple(participant_list)
    print("Order tuple:", order_details)


    list_mix = ['H1', 'H100', 'H10', 'H3', 'H2', 'H6', 'H11', 'H50', 'H5', 'H99', 'H8']
    
    # ? Ordenar letras y numeros
    order_mix = order_str_num(list_mix)
    print("Order list:",order_mix)


    dictionary = {"Estela" : 900, "Edison" : 800, "Carlos" : 650, "Juan" : 600}

    # ? Ordenar por salario
    dict_order = order_dict(dictionary)
    print("Order dict:",dict_order)

