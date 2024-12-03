import mysql.connector
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

def cargar_datos(tree):
    # Conectar a la base de datos MySQL en WAMPServer
    try:
        connection = connect_db()
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Consulta SQL para obtener los datos de la tabla
            query = "SELECT id_libro, titulo, autor, editorial, categoria, estado FROM libros"
            cursor.execute(query)

            # Recuperar todos los resultados
            rows = cursor.fetchall()

            # Limpiar el Treeview antes de insertar nuevos datos
            for row in tree.get_children():
                tree.delete(row)

            # Insertar los resultados en el Treeview
            for row in rows:
                tree.insert("", "end", values=row)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insertar_dato(codigo, titulo, autor, editorial, categoria, estado):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO libros (id_libro, titulo, autor, editorial, categoria, estado)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (codigo, titulo, autor, editorial, categoria, estado)
    cursor.execute(query, values)
    
    connection.commit()
    cursor.close()
    connection.close()

def eliminar_dato(isbn):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "DELETE FROM libros WHERE id_libro = %s"
    cursor.execute(query, (isbn,))
    
    connection.commit()
    cursor.close()
    connection.close()

def obtener_datos():
        # Conectar a la base de datos SQLite
        connection = connect_db()
        cursor = connection.cursor()
        
        query = "SELECT id_libro, titulo, autor, editorial, categoria, estado FROM libros"
        
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados

def obtener_libros():
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT titulo FROM libros")
    
    libros = cursor.fetchall()
    
    connection.close()
    return [titulo[0] for titulo in libros]