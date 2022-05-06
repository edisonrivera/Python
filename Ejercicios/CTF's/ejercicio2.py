from random import randrange
def values():
    number = 6
    random_number = 0
    while random_number != number:
        random_number = randrange(1,number+1)
        print(f"{random_number}" if random_number != number else "TERMINÓ")
values()