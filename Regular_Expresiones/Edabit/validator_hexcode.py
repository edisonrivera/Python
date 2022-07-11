from re import IGNORECASE, search


def is_valid_hex_code(hex_code: str) -> bool:
    pattern = "^#[a-f0-9]{6}"
    return True if(search(pattern, hex_code, IGNORECASE)) else False

if __name__ == "__main__":
    hex_code = input("-> Your hexcode: ").strip()
    print("The code is valid?:",is_valid_hex_code(hex_code))