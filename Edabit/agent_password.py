from re import search

def secret_password(str_to_encode: str) -> str:
    pattern = "[A-Z!-\+\.\^\$#]"
    if (not(search(pattern, str_to_encode)) and len(str_to_encode) == 9):
        first_part = encoded_first_part(str_to_encode[:3])
        second_part = enconded_second_part(str_to_encode[3:6])
        third_part = enconded_third_part(str_to_encode[6:9])
        return (second_part + third_part + first_part)
    return "BANG! BANG! BANG!"

def encoded_first_part(first_part: str) -> str:
    f_int = ord(first_part[0]) - 96
    s_int = ord(first_part[2]) - 96
    return (str(f_int) + first_part[1] + str(s_int))

def enconded_second_part(second_part: str) -> str:
    return ("".join(second_part[::-1]))

def enconded_third_part(third_part: str) -> str:
    new_part = ""
    for letter in third_part:
        if (letter == 'z'):
            new_part += 'a'
        else:
            new_part += chr(ord(letter)+1)
    return new_part


if __name__ == "__main__":
    to_encode = "mattedabi"
    encoded_str = secret_password(to_encode)
    print("Encoded:",encoded_str)