from re import sub


def switcheroo (words : list, phrase: str) -> str:
    return sub(f"{words[0]}",words[1],phrase)
    
if __name__ == "__main__":
    words_replace = ["nts", "nce"]
    phrase_user = "The elephants in France were chased by ants!"
    phrase_switch = switcheroo(words_replace, phrase_user)
    print("Final phrase:", phrase_switch)