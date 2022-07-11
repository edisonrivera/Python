def secret(str_phrase: str) -> str:
    list_symbols = [">", ".", "*"]
    list_labels = list()
    repeat_label = int(str_phrase[-1])

    for symbol in list_symbols:
        label = str_phrase.split(symbol)[0]
        str_phrase = str_phrase.replace(label+symbol,"")
        list_labels.append(label)

    phrase_final = build_secret_phrase(list_labels,repeat_label)
    return phrase_final


def build_secret_phrase(list_labels: list, repeat: int) -> str:
    phrase = ""
    number_zeros = "0" * (list_labels[2].count("$") - 1)
    letter_class = list_labels[2][0]
    phrase += f"<{list_labels[0]}>\n"

    for times in range(repeat):
        phrase += f"\t<{list_labels[1]} class=\"{letter_class + number_zeros + str(times +1)}\"></{list_labels[1]}>\n"
    
    phrase += f"</{list_labels[0]}>"
    
    return phrase

if __name__ == "__main__":
    str_user = "div>p.c$$$*7"
    str_converted = secret(str_user)
    print(str_converted)