from re import match, sub


def decrypt(str_to_encrypt: str) -> str:
    pattern = "(\d{2})#"

    phrase = ""
    if(matches:= match(pattern, str_to_encrypt)):
        list_numbers_to_convert = matches.groups()
        band = (str_to_encrypt.startswith(list_numbers_to_convert[0]))
        for item in list_numbers_to_convert:
            phrase += chr(int(item) + 96)


    if(matches:= sub(pattern,"",str_to_encrypt)):
        to_convert = matches
        
        
    if band:
        for value in to_convert:
            phrase += chr(int(value) + 96)
    return phrase

if __name__ == "__main__":
    str_user = "10#11#12"
    encrypted = decrypt(str_user)
    print("Encrypted:", encrypted)