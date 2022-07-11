from re import search


def scrambled(words:list, model:str) -> list:
    pattern = model.replace("*",".")
    print(pattern)
    list_word = list(filter(lambda word: search(pattern, word) and (len(word) == len(pattern)),words))
        
    return list_word

if __name__ == "__main__":
    model = "***"
    words_list = ["red", "dee", "cede", "reed", "creed", "decree"]
    list_concidences = scrambled(words_list, model)
    print("Final list:", list_concidences)