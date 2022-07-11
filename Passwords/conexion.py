import sqlite3
class Data_Base():
    def __init__(self) -> None:
        self.name_db = "passwords"
        self.ruta = f"C:\\Users\\pc\\Cursos_de_Programacion\\Python\\Passwords\\Base_Datos\\{self.name_db}.db"
        self.conexion_db = sqlite3.connect(self.ruta)
        self.cursor = self.conexion_db.cursor()


    def create_table(self):
        table_site = """
        CREATE TABLE IF NOT EXISTS site ( 
            id integer PRIMARY KEY,
            sitio VARCHAR(25) NOT NULL,
            password VARCHAR(50) NOT NULL
        );
        """

        self.cursor.execute(table_site);


    def send_dates(self, site, password):
        instruccion = "INSERT INTO site (sitio, password) VALUES (?,?)"
        self.cursor.execute(instruccion, (site, password))
        self.conexion_db.commit()
    
    def close_db(self):
        self.conexion_db.close()