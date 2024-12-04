import mysql.connector
from tkinter import messagebox as mb
from mysql.connector import Error

# Conexion
def connect_db():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', passwd='', database='Biblioteca')
        return connection
    except Error as err:
        print(f'Error al conectar la base de Datos {err}')
        return None

# Verificacion de Credenciales
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

# CRUD
def Insertar_Datos(codigo, titulo, autor, editorial, categoria, estado):
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
def Insertar_Prestamos(codigo, nombre, titulo, fecha_prestamo, fecha_devolucion):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = """
    INSERT INTO prestamos (id_usuario, nombre, titulo, fecha_prestamo, fecha_devolucion)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (codigo, nombre, titulo, fecha_prestamo, fecha_devolucion)
    cursor.execute(query, values)
    
    connection.commit()
    cursor.close()
    connection.close()
def Insertar_Devolucion(codigo, nombre, titulo, fecha_devolucion, fecha_devolucion_real):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "INSERT INTO devoluciones (id_usuario, nombre, titulo, fecha_devolucion, fecha_devolucion_real) VALUES (%s, %s, %s, %s, %s)"
    values = (codigo, nombre, titulo, fecha_devolucion, fecha_devolucion_real)
    cursor.execute(query, values)
    
    connection.commit()
    cursor.close()
    connection.close()
def Insertar_Sancion(codigo, usuario, monto, fecha):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "INSERT INTO multas (id_multa, id_usuario, monto_multa, fecha_multa) VALUES (%s, %s, %s, %s)"
    values = (codigo, usuario, monto, fecha)
    cursor.execute(query, values)
    
    connection.commit()
    cursor.close()
    connection.close()
def Eliminar_Datos(isbn):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "DELETE FROM libros WHERE id_libro = %s"
    cursor.execute(query, (isbn,))
    
    connection.commit()
    cursor.close()
    connection.close()
def Eliminar_Sancion(codigo):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "DELETE FROM multas WHERE id_usuario = %s"
    cursor.execute(query, (codigo,))
    
    connection.commit()
    cursor.close()
    connection.close()
def Eliminar_Prestamo(codigo):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "DELETE FROM prestamos WHERE id_usuario = %s"
    cursor.execute(query, (codigo,))
    connection.commit()

# Gets
def Obtener_Datos():
        connection = connect_db()
        cursor = connection.cursor()
        
        query = "SELECT id_libro, titulo, autor, editorial, categoria, estado FROM libros"
        
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados
def Consulta_Prestamos():
        connection = connect_db()
        cursor = connection.cursor()
        
        query = "SELECT id_usuario, nombre, titulo, fecha_prestamo, fecha_devolucion FROM prestamos"
        
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados
def Consulta_Devoluciones():
        connection = connect_db()
        cursor = connection.cursor()
        
        query = "SELECT id_usuario, nombre, titulo, fecha_devolucion, fecha_devolucion_real FROM devoluciones"
        
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados
def Consulta_Sanciones():
        connection = connect_db()
        cursor = connection.cursor()
        
        query = "SELECT id_multa, id_usuario, monto_multa, fecha_multa FROM multas"
        
        cursor.execute(query)
        
        resultados = cursor.fetchall()
        connection.close()
        return resultados
def Obtener_Prestamos(id_usuario):
        connection = connect_db()
        cursor = connection.cursor()
    
        # Consultar los préstamos de un usuario específico
        query = "SELECT id_usuario, nombre, titulo, fecha_prestamo, fecha_devolucion FROM prestamos WHERE id_usuario = %s"
    
        cursor.execute(query, (id_usuario,))
    
        resultados = cursor.fetchall()
        connection.close()
        return resultados
def Obtener_Libros():
    connection = connect_db()
    cursor = connection.cursor()
    
    cursor.execute("SELECT titulo FROM libros")
    
    libros = cursor.fetchall()
    
    connection.close()
    return [titulo[0] for titulo in libros]

# Cargar Info
def Cargar_Datos(tree):
    try:
        connection = connect_db()
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id_libro, titulo, autor, editorial, categoria, estado FROM libros"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in tree.get_children():
                tree.delete(row)

            for row in rows:
                tree.insert("", "end", values=row)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def Cargar_Prestamos(tree):
    try:
        connection = connect_db()
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id_usuario, nombre, titulo, fecha_prestamo, fecha_devolucion FROM prestamos"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in tree.get_children():
                tree.delete(row)

            for row in rows:
                tree.insert("", "end", values=row)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
def Cargar_Devoluciones(tree):
    try:
        connection = connect_db()
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id_usuario, nombre, titulo, fecha_devolucion, fecha_devolucion_real FROM devoluciones"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in tree.get_children():
                tree.delete(row)

            for row in rows:
                tree.insert("", "end", values=row)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
def Cargar_Sanciones(tree):
    try:
        connection = connect_db()
        
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT id_multa, id_usuario, monto_multa, fecha_multa FROM multas"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in tree.get_children():
                tree.delete(row)

            for row in rows:
                tree.insert("", "end", values=row)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")