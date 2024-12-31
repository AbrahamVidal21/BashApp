import sqlite3

class Conexion:
    @staticmethod
    def conexionDataBase():
        try:
            conexion = sqlite3.connect('SqliteDB.db')
            return conexion  # Retorna la conexión para su uso posterior
        except sqlite3.Error as error:
            print(f'Error al conectar con la base de datos: {error}')
            return None


