from re import sub


def clean_str (str_user: str) -> str:
    words_sorted = sorted(str_user.split(" "), key=lambda x: int("".join([i for i in x if i.isdigit()])))
    pattern = "[0-9]"
    fix_words_list = sub(pattern,""," ".join(words_sorted))
    return "".join(fix_words_list)


if __name__ == "__main__":
    str_user = "en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves".strip()
    str_clean = clean_str(str_user)
    print("Str:",str_clean)