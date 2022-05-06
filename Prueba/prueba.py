from genericpath import isdir
from os import getcwd, listdir
from cryptography.fernet import Fernet

def generate_key():
    key_o = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key_o)

def load_key():
    return open("key.key","rb").read()

def encrypt_anyone(pathEnc,k):
    to_encrypt = listdir(pathEnc)
    print(to_encrypt)
    


if __name__ == "__main__": 
    real_path = getcwd()
    generate_key()
    key = load_key()
    encrypt_anyone(real_path,key)
    #print(listdir(r"C:\Users\pc\Python\Prueba\prueba.py"))
    print(isdir(r"C:\Users\pc\Python\Prueba\prueba.py"))
