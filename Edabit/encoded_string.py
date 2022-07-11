import re


def parse_code(to_decode: str):
    dates_decode = re.findall(r"^[)a-zA-Z)]+0", to_decode)
    print (dates_decode)

if __name__ == "__main__":
    parse_code("Hola0ja00kil")