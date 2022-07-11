import sqlite3 as sql


def create_database():
    conexion = sql.connect("streamers.db")
    conexion.commit()
    conexion.close()

def create_table():
    conexion = sql.connect("streamers.db")
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS streamers(
        id integer PRIMARY KEY,
        nombre VARCHAR(25) NOT NULL,
        suscriptores INT NOT NULL
    )""")

    nombre = "Ibai"
    subs = 15000
    conexion.execute(f"INSERT INTO streamers (nombre, suscriptores) VALUES (?,?)", (nombre,subs))
    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    create_database()
    create_table()