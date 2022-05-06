from random import sample
from time import sleep

class Passwords():

    def __init__ (self,file_name = "PASSWORDS MANAGER.txt"):
        self.file_name = file_name

    def get_name_file(self):
        if self.comprobar_archivo():
            self.get_name_file()

    def change_name_file(self):
        pass

    def comprobar_archivo(self):
        try:
            print("Preparando todo...")
            sleep(2)
            bool_file = open(f"{self.file_name}","x")
            #bool_file.write("|" + "SOCIAL MEDIA / WEBSITE".center(25," ") + "|" + "PASSWORD".center(25, " ") + "|\n")
            #bool_file.write("_____________________________________________________\n")
            bool_file.close()
            return True
        except FileExistsError:
            print("!! El nombre del archivo se encuentra ocupado !!")
            return False

    def generate_password(self):
        letters = "abcdefghijklmnopqrstuwxyz"
        numbers = "1234567890"
        special_characters = "[]{}@|_:.,=$&%!¡#/*-+"
        password_list = letters + numbers + special_characters
        key = sample(password_list,10)
        print("Generando contraseña...")
        sleep(2)
        return "".join(key)

    def swFile(self):
        verificador = ""
        file_name = self.get_name_file()
        file_manager = open(f"{file_name}","a")
        while verificador == "Y":
            password = self.generate_password()
            website = input("-> Sitio web: ")
            file_manager.write("|" + f"{website}".center(25," ") + "|" + f"{password}".center(25," ") + "|\n")
            verificador = input("Desea generar otra contreseña (Y/N): ")
        file_manager.close()

if __name__ == "__main__":         
    generar = Passwords()
    generar.swFile()