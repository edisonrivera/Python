import re


def is_parse_tongue(phrase: str):
    pattern_split = "\s+?"
    lists_wordsss = re.split(pattern_split, phrase)
    pattern_validate = "s{2,10}"
    band = True
    for word in lists_wordsss:
        if ("s" in word):
            if (not re.search(pattern_validate, word,re.IGNORECASE)):
                band = False
                break
    return band


if __name__ == "__main__":
    languaje_ssserpents = input("-> Phrase ssserpents: ").strip()
    is_valid = is_parse_tongue(languaje_ssserpents)
    print("The phrase is valid?", is_valid)