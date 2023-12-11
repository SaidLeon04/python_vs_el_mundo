import mysql.connector

def conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="nergy"
        )
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            return conexion  # Retorna la conexión para usar en otro archivo
    except mysql.connector.Error as error:
        print("Error al conectar a MySQL:", error)
        return None
