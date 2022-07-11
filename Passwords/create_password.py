from random import sample

def generate_password():
    letters = "abcdefghijklmnopqrstuwxyz"
    numbers = "1234567890"
    special_characters = "[]{}@|_:.,=$&%!¡#/*-+"
    password_list = letters + numbers + special_characters
    key = sample(password_list,10)
    return "".join(key)

if __name__ == "__main__":
    password = generate_password()
    print(password)