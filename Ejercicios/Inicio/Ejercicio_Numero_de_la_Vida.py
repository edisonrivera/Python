def is_numeric():
    band = True
    result = 0
    date_to_evaluate = input("-> DATE: ")
    if date_to_evaluate.isdigit():
        while band:
            for i in str(date_to_evaluate):
                result += int(i)
                date_to_evaluate = result
            if (result >= 10): result = 0
            else: band = False
        print("-> NUMBER LIFE: ", result)
    else:
        print("Try Again!")

is_numeric()