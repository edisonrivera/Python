def replace_varius(str_replaces:str,list_words:list,replace_by:str) -> str:
    for word in list_words:
        if (word in str_replaces):
            str_replaces = str_replaces.replace(word,replace_by*len(word))

    return str_replaces


if __name__ == "__main__":
    str_user = "The cow jumped over the moon."
    list_words = ["cow", "over"]
    replace_by = "*"
    str_ready = replace_varius(str_user,list_words,replace_by)
    print("Final str:",str_ready)