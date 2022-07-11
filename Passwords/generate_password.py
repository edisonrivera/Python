from random import sample


def generate_password(longitud_password: int) -> str:
    letters = "abcdefghijklmnopqrstuwxyz"
    numbers = "1234567890"
    special_characters = "[]{}@|_:.,=$&%!¡#/*-+"
    password_list = letters + numbers + special_characters
    key = sample(password_list,longitud_password)
    return "".join(key)

if __name__ == "__main__":
    while True:
        try:
            longitud = int(input("- Longitud password: "))
            break
        except ValueError:
            print("Inténtalo de nuevo !")
    password = generate_password(longitud)
    print(password)