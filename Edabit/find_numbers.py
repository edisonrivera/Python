from re import findall

def integers_list(str_user: str) -> list:
    pattern = "[0-9]"
    return findall(pattern, str_user)


if __name__ == "__main__":
    text = " 123.456 2 +7 -88 -.25 9.10.11 -4. +-34 -0.6 --5 "
    int_list = integers_list(text)
    print("Integers:", int_list)