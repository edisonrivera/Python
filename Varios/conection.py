import sqlite3

def connect_to_db():
    conexion = sqlite3.connect('registro')
    cursor = conexion.cursor()
    
    # cursor.execute('''CREATE TABLE credenciales ( 
    #     id integer PRIMARY KEY,
    #     sitio VARCHAR(25) NOT NULL,
    #     password VARCHAR(50) NOT NULL
    # );''')
    
    return cursor, conexion


def try_send_datos(cursor, conexion):
    # sitio = input("-> Sitio web: ")
    # password = input("-> Clave: ")
    # cursor.execute(f"INSERT INTO credenciales (sitio,password) VALUES (?,?)",(sitio,password))
    cursor.execute("SELECT * FROM datos")
    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    cr, cx = connect_to_db()
    try_send_datos(cr,cx)