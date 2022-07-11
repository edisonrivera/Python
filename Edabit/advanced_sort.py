def advanced_sort(list_to_order: list) -> list:
    # ? Order the list
    list_to_order = sorted(list_to_order, reverse=True)

    # * n list to create
    number_of_lists =len(set(list_to_order))

    # ? Create n lists as values are different
    list_final = list()
    for c_l in range (number_of_lists):
        list_final.append(list())


    # * Take the first values of the principal list
    first_item = list_to_order[0]
    index = 0
    for item in list_to_order:
        # ? Function: Compare the first value with the next value, if the next
        # ? value is different this is almacenate in the next list, else, the
        # ? current value is almacenate in the current list 
        if (first_item != item):
            index += 1
            list_final[index].append(item)
            first_item = item
        else:
            list_final[index].append(item)
    
    return list_final


if __name__ == "__main__":
    list_user = [1,2,3]
    list_order = advanced_sort(list_user)
    print("Order list:", list_order)