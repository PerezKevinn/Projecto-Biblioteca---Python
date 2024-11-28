import mysql.connector
import menu
from tkinter import messagebox as mb
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', passwd='', database='Biblioteca')
        return connection
    except Error as err:
        print(f'Error al conectar la base de Datos {err}')
        return None
    
def login(username, password):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM users WHERE user = %s AND pass = %s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        
        if user:
            mb.showinfo(title='Ingreso exitoso', message=f'Bienvenido {username}')
            return True
        else:
            mb.showerror(title='Verificar credenciales', message='El usuario y/o contraseña son incorrectos')
            return False
    else:
        mb.showerror(title='Error de conexion', message='Error al conectar con la base de datos')
    cursor.close()
    connection.close()