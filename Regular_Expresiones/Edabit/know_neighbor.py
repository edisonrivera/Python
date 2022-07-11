from re import IGNORECASE, search


def plus_sign(str_analize : str) -> bool:
    pattern_comprobate = "(\+\++|\w\w+)"
    if (search(pattern_comprobate, str_analize, IGNORECASE)):
        return False
    return True

if __name__ == "__main__":
    str_user = "+s+7+fg+r+8+"
    bool_condition = plus_sign(str_user)
    print("Condition is valid?",bool_condition)