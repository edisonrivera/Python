from re import findall

if __name__ == "__main__":
    lista = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie", 
            "bad cookie", "bad cookie", "bad cookie", "bad cookie", "good cookie",
            "bad cookie", "good cookie"]

    pattern = "\s?b[a-z]+\s"
    print(len(findall(pattern,", ".join(lista))))