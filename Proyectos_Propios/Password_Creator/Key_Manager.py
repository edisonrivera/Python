from random import sample
from sys import path
from os import strerror
import readchar

#Variables
letters = "abcdefghijklmnopqrstuwxyz"
numbers = "1234567890"
special_characters = "[]{}@|_:.,=$&%!¡#/*-+"
key_list = letters + numbers + special_characters

def create_file():
    try:
        passwords_file = open(f"{path[0]}\\pass_file.txt","w")
        passwords_file.close()
    except Exception as err:
        print("¡ERROR TO CREATE A FILE!",strerror(err.errno))


def make_pass():
    verificator = "Y"
    while verificator == "Y":
        lista = input("Ingrese los parametros solicitados: ")
        website, longitud = lista.split(" ")
        passwords_file = open(f"{path[0]}\\pass_file.txt","wr")
        if passwords_file.readline() == "":
            passwords_file.write("|" + "SOCIAL MEDIA / WEBSITE".center(25," ") + "|" + "PASSWORD".center(25, " ") + "|\n")
            passwords_file.write("_____________________________________________________\n")
        password = sample(key_list,int(longitud))
        password = "".join(password)
        passwords_file = open(f"{path[0]}\\pass_file.txt","a")
        passwords_file.write("|" + f"{website}".center(25," ") + "|" + f"{password}".center(25," ") + "|\n")
        print("[+] Clave generada...")
        verificator = input("Do you want to create a new pass (Y/N): ")
    else:
        print("[-] Saliendo del programa...")
    passwords_file.close()

create_file()
make_pass() 