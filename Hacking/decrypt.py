import os 
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if (file == "ransomware.py" or file == "thekey.key" or file == "decrypt_key"):
        continue
    if (os.path.isfile(file)):
        files.append(file)


# Read key
with open("thekey.key", "rb") as thekey:
    decrypt_key = thekey.read()

for file in files:
    with open(file,"rb") as thefile:
        content = thefile.read()
    content_to_decrypt = Fernet(decrypt_key).decrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_to_decrypt)