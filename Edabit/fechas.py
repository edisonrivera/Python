def convert_date(date: str) -> str:
    return "".join(date.split('/'))[::-1]

if __name__ == '__main__':
    date_format = input("-> Date: ")
    str_date = convert_date(date_format)
    print("-> Date convert:", str_date)