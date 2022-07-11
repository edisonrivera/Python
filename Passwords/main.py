from conexion import Data_Base
from create_password import generate_password



def insert_dates():
    verificador = "S"
    while (verificador != "N"):
        site = input("- Sitio Web: ")
        verificar_pass = input("- Automatic Password (S/N): ")
        if (verificar_pass == "S"):
            password = generate_password()
        else:
            password = input("- Password: ")
        db.send_dates(site, password)
        verificador = input("- Desea continuar? (S/N): ")
    

if __name__ == "__main__":
    db = Data_Base()
    db.create_table()
    insert_dates()
    db.close_db()