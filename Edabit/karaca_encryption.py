def karaca_encrypt(initial_word: str):
    dictionaty = {"a" : "0","e" : "1","i" : "2","o" : "2","u" : "3"}
    to_encrypt = initial_word[::-1]

    for key in dictionaty.keys():
        if (key in to_encrypt):            
            to_encrypt = to_encrypt.replace(key, dictionaty[key])
            
    to_encrypt += "aca"
    print (to_encrypt) 


if __name__ ==  "__main__":
    word = input("Word: ")
    karaca_encrypt(word)