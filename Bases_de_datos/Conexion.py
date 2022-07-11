import mysql.connector
from mysql.connector import Error

def try_connect():
    try:
        conexion = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = "root",
            password = "HoLa@outlook18",
            db = 'registro'
        ) 

    except Error as ex:
        print ("ERROR: ", ex)
        conexion.close()
    return conexion

    

if __name__ == "__main__":
    conexion = try_connect()
    if conexion:
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM datos")

        # fetachall() -> Seleccionar todos los registros.
        registro = cursor.fetchall()
        # registro=cursor.fetchone()
        print("Conectado a la BD:", registro)