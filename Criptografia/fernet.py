from cryptography.fernet import Fernet

# ! Generar llave Fernet
key = Fernet.generate_key()

# ? Valor de la llave asignado a una variable
f = Fernet(key)

# ? Tenemos que transformar a bytes
# TODO -> encrypt(data)           [ data (bytes) ]
mensaje = b"Hola Amorlais"

# ? Encriptar los datos 
encrypt = f.encrypt(mensaje)
print(encrypt)

# ? Desencriptar los datos
decrypt = f.decrypt(encrypt)
print(decrypt)