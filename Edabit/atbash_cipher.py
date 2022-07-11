def atbash(str_user : str) -> str:
    new_word = ""
    for letter in str_user:
        if (letter.isalpha()):
            chr_letter = ord(letter)
            if (97 <= chr_letter <= 122):
                difference = chr_letter - 97
                int_letter = 122 - difference
            else:
                difference = chr_letter - 65
                int_letter = 90 - difference
            new_word += chr(int_letter)
        else:
            new_word += letter
    return new_word


if __name__ == "__main__":
    word = "Hello world!"
    word_atbash = atbash(word)
    print("New word:", word_atbash)