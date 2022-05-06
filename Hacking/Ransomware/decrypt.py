import os
from cryptography.fernet import Fernet
def cargar_key():
    return open("key.key", "rb").read()

def decrypt (items,key):
    f = Fernet(key)
    for item in items:
        with open(item,"rb") as file:
            encrypt_data = file.read()
        decrypt_data = f.decrypt(encrypt_data)
        with open(item, "wb") as file:
            file.write(decrypt_data)

if __name__ == "__main__":
    path_to_encrypt = "C:\\Users\\pc\\Python\\Otros\\Ransomware\\Carpeta_Normal"
    os.remove(path_to_encrypt+"\\"+"readme.txt")
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+"\\"+item for item in items]
    key = cargar_key()
    decrypt(full_path,key)