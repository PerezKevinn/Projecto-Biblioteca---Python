import tkinter as tk
import customtkinter as ctk
import tooltip
import conexion
import login
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image

class App():
    def __init__(self):
        
        
        
        # Ventana Principal
        self.FrmMenu = tk.Tk()
        self.FrmMenu.title("Menu Principal")
        self.FrmMenu.config(background='#002029')
        self.FrmMenu.resizable(False,False)
        
        # Variables Main
        SpFoto = Image.open('img/pic/profile.png')
        SpInventario = Image.open('img/icon/inventory.png')
        SpPrestamos = Image.open('img/icon/loans.png')
        SpDevoluciones = Image.open('img/icon/return.png')
        SpSanciones = Image.open('img/icon/sanctions.png')
        SpInformes = Image.open('img/icon/informes.png')
        SpSalir = Image.open('img/icon/exit.png')
        
        # Variables Inventario
        SpNuevo = Image.open('img/icon/add.png')
        SpEditar = Image.open('img/icon/update.png')
        SpEliminar = Image.open('img/icon/delete.png')
        SpBuscar = Image.open('img/icon/search.png')
        
        # Variables Prestamos
        SpGuardar = Image.open('img/icon/save.png')
        SpCancelar = Image.open('img/icon/cancel.png')
        SpInicio = Image.open('img/icon/inicio.png')
        SpConsultar = Image.open('img/icon/buscar.png')
        SpRegistrar = Image.open('img/icon/registrar.png')
        
        # Imagenes
        self.Foto = ctk.CTkImage(light_image=SpFoto, dark_image=SpFoto, size=(128,128))
        self.Inventario = ctk.CTkImage(light_image=SpInventario, dark_image=SpInventario, size=(32,32))
        self.Prestamos = ctk.CTkImage(light_image=SpPrestamos, dark_image=SpPrestamos, size=(32,32))
        self.Devoluciones = ctk.CTkImage(light_image=SpDevoluciones, dark_image=SpDevoluciones, size=(32,32))
        self.Sanciones = ctk.CTkImage(light_image=SpSanciones, dark_image=SpSanciones, size=(32,32))
        self.Informes = ctk.CTkImage(light_image=SpInformes, dark_image=SpInformes, size=(32,32))
        self.Salir = ctk.CTkImage(light_image=SpSalir, dark_image=SpSalir, size=(32,32))
        
        # Imagenes Botones Inventario
        self.Nuevo = ctk.CTkImage(light_image=SpNuevo, dark_image=SpNuevo, size=(32,32))
        self.Editar = ctk.CTkImage(light_image=SpEditar, dark_image=SpEditar, size=(32,32))
        self.Eliminar = ctk.CTkImage(light_image=SpEliminar, dark_image=SpEliminar, size=(32,32))
        self.Buscar = ctk.CTkImage(light_image=SpBuscar, dark_image=SpBuscar, size=(32,32))
        
        # Imagenes Prestamos
        self.Guardar = ctk.CTkImage(light_image=SpGuardar, dark_image=SpGuardar, size=(32,32))
        self.Cancelar = ctk.CTkImage(light_image=SpCancelar, dark_image=SpCancelar, size=(32,32))
        self.Inicio = ctk.CTkImage(light_image=SpInicio, dark_image=SpInicio, size=(32,32))
        self.Consultar = ctk.CTkImage(light_image=SpConsultar, dark_image=SpConsultar, size=(32,32))
        self.Registrar = ctk.CTkImage(light_image=SpRegistrar, dark_image=SpRegistrar, size=(32,32))
        
        # Llamar Funciones
        self.centerWindow()
        self.Paneles()
        self.Controles_Panel_Lateral()
        self.FrmMenu.mainloop()
    
    # Funciones
    def centerWindow(self):
        W, H = 1200, 700
        
        Ws = (self.FrmMenu.winfo_screenwidth()//2) - (W//2)
        Hs = (self.FrmMenu.winfo_screenheight()//2) - (H//2)
        
        self.FrmMenu.geometry(f'{W}x{H}+{Ws}+{Hs}')

    # Paneles
    def Paneles(self):
        # Menu lateral
        self.FrNav = ctk.CTkFrame(self.FrmMenu, width=200, height=698, fg_color='#005066', corner_radius=0)
        self.FrNav.pack(side=ctk.LEFT)
        
        # Frame Pages
        self.FrPages = ctk.CTkFrame(self.FrmMenu, width=1000, height=698, fg_color='#002029', corner_radius=0)
        self.FrPages.pack(side=ctk.LEFT)

    # Formularios
    def Inventory_Panel(self):
        # Frame de Inventario
        self.FrInventory = tk.Frame(self.FrPages, background='#002029', width=900, height=800)
        self.FrInventory.place(relx=0.05, rely=0)
        self.FrInventory.grid_propagate(False)
        
        # Frame Botones
        self.FrButtons = ctk.CTkFrame(self.FrInventory, width=800, height=120, corner_radius=30, fg_color='#005066')
        self.FrButtons.place(relx=0.05, rely=0.03)
        
        # Consulta
        self.TxtConsulta = ctk.CTkEntry(self.FrButtons, width=400, fg_color='#FFFFFF', font=('Roboto', 18), text_color='#000000', placeholder_text='ISBN / ID / NOMBRE', placeholder_text_color='#a1a0a0')
        self.TxtConsulta.place(relx=0.26, rely=0.40)
        self.TxtConsulta.bind("<KeyRelease>", self.Consulta_Libros)
        
        # Frame Grilla
        self.FrGrilla = ctk.CTkFrame(self.FrInventory, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrGrilla.place(relx=0.05, rely=0.20)
        
        # Treeview
        self.Tree = ttk.Treeview(self.FrGrilla, columns=('ISBN', 'Titulo', 'Autor', 'Editorial', 'Categoria', 'Estado'))
        
        # Configurar los headings
        self.Tree.heading("#0", text="")
        self.Tree.heading("ISBN", text="ISBN")
        self.Tree.heading("Titulo", text="Título")
        self.Tree.heading("Autor", text="Autor")
        self.Tree.heading("Editorial", text="Editorial")
        self.Tree.heading("Categoria", text="Categoría")
        self.Tree.heading("Estado", text="Estado")
        
        # Configurar la columna
        self.Tree.column("#0", width=0)
        self.Tree.column("ISBN", width=100)
        self.Tree.column("Titulo", width=160)
        self.Tree.column("Autor", width=140)
        self.Tree.column("Editorial", width=120)
        self.Tree.column("Categoria", width=80)
        self.Tree.column("Estado", width=100)
        
        # Posicionar el Tree
        self.Tree.place(relx=0.06, rely=0.20)
        
        # Llenar datos
        conexion.Cargar_Datos(self.Tree)
        
        self.BtnNuevo = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Nuevo, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.Agregar_Registro)
        self.BtnNuevo.place(relx=0.13, rely=0.06)
        tooltip.Hovertip(self.BtnNuevo, text='Agregar nuevo registro', hover_delay=100)
        
        self.BtnEliminar = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Eliminar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.Eliminar_Registro)  
        self.BtnEliminar.place(relx=0.33, rely=0.06)
        tooltip.Hovertip(self.BtnEliminar, text='Eliminar registro seleccionado', hover_delay=100)
    def Loans_Form(self): 
        # Frame Prestamos
        self.FrLoans = tk.Frame(self.FrPages, background='#002029', width=900, height=800)
        self.FrLoans.place(relx=0.05, rely=0)
        self.FrLoans.grid_propagate(False)
        
        # Frame Botones
        self.FrButtons = ctk.CTkFrame(self.FrLoans, width=800, height=120, corner_radius=30, fg_color='#005066')
        self.FrButtons.place(relx=0.05, rely=0.03)
        
        # Frame Datos
        self.FrDatos = ctk.CTkFrame(self.FrLoans, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrDatos.place(relx=0.05, rely=0.20)
        
        # Btn Consultar
        self.BtnConsultar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Consultar, text='Consultar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Search)
        self.BtnConsultar.place(relx=0.25, rely=0.18)
        
        # Btn Registrar
        self.BtnRegistrar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Registrar, text='Registrar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Add)
        self.BtnRegistrar.place(relx=0.50, rely=0.18)
    def Returns_Form(self):
        # Frame Devoluciones
        self.FrReturns = tk.Frame(self.FrPages, background='#002029', width=900, height=800)
        self.FrReturns.place(relx=0.05, rely=0)
        self.FrReturns.grid_propagate(False)
        
        # Frame Botones
        self.FrButtons = ctk.CTkFrame(self.FrReturns, width=800, height=120, corner_radius=30, fg_color='#005066')
        self.FrButtons.place(relx=0.05, rely=0.03)
        
        # Frame Datos
        self.FrDatos = ctk.CTkFrame(self.FrReturns, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrDatos.place(relx=0.05, rely=0.20)
        
        # Btn Consultar
        self.BtnConsultar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Consultar, text='Consultar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Search_Devoluciones)
        self.BtnConsultar.place(relx=0.25, rely=0.18)
        
        # Btn Registrar
        self.BtnRegistrar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Registrar, text='Registrar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Add_Devoluciones)
        self.BtnRegistrar.place(relx=0.50, rely=0.18)
    def Sanctions_Form(self):
        # Frame Sanciones
        self.FrSanctions = tk.Frame(self.FrPages, background='#002029', width=900, height=800)
        self.FrSanctions.place(relx=0.05, rely=0)
        self.FrSanctions.grid_propagate(False)
        
        # Frame Botones
        self.FrButtons = ctk.CTkFrame(self.FrSanctions, width=800, height=120, corner_radius=30, fg_color='#005066')
        self.FrButtons.place(relx=0.05, rely=0.03)
        
        # Frame Datos
        self.FrDatos = ctk.CTkFrame(self.FrSanctions, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrDatos.place(relx=0.05, rely=0.20)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrButtons, text='Ingresar codigo', text_color='#FFFFFF',  bg_color='#005066', width=120, height=4, font=('Roboto', 18, 'bold'))
        self.LblCodigo.place(relx=0.20, rely=0.40)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrButtons, text_color='#000000', fg_color='#FFFFFF', width=290, height=4, font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.40, rely=0.40)
        self.TxtCodigo.bind("<KeyRelease>", self.Consulta_Sanciones)
        
        # Treeview
        self.Tree = ttk.Treeview(self.FrDatos, columns=('CODIGO', 'USUARIO', 'MONTO', 'FECHA'))
        
        # Configurar los headings
        self.Tree.heading("#0", text="")
        self.Tree.heading("CODIGO", text="Codigo")
        self.Tree.heading("USUARIO", text="Id Usuario")
        self.Tree.heading("MONTO", text="Monto")
        self.Tree.heading("FECHA", text="Fecha")

        # Configurar la columna
        self.Tree.column("#0", width=0)
        self.Tree.column("CODIGO", width=100)
        self.Tree.column("USUARIO", width=150)
        self.Tree.column("MONTO", width=140)
        self.Tree.column("FECHA", width=140)
        
        # Posicionar el Tree
        self.Tree.place(relx=0.17, rely=0.10)

        # Nuevo
        self.BtnNuevo = ctk.CTkButton(self.FrDatos, width=60, height=50, image=self.Nuevo, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.Agregar_Sancion)
        self.BtnNuevo.place(relx=0.06, rely=0.10)
        tooltip.Hovertip(self.BtnNuevo, text='Agregar nuevo registro', hover_delay=100)
        
        # Eliminar
        self.BtnEliminar = ctk.CTkButton(self.FrDatos, width=60, height=50, image=self.Eliminar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.Eliminar_Sanciones)
        self.BtnEliminar.place(relx=0.06, rely=0.30)
        tooltip.Hovertip(self.BtnEliminar, text='Eliminar registro seleccionado', hover_delay=100)
        
        # Cargar Datos
        conexion.Cargar_Sanciones(self.Tree)
        
    # Frames
    def Create_Search(self):
        self.delete_frdatos()
        # Cambiar Boton
        self.BtnConsultar.configure(image=self.Inicio, text='Inicio', command=self.Home_Prestamos)
        if (self.BtnRegistrar.cget('image') == self.Inicio):
            self.BtnRegistrar.configure(image=self.Registrar, text='Registrar', command=self.Create_Add)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrDatos, width=120, font=('Roboto', 18), text='Ingrese el codigo:')
        self.LblCodigo.place(relx=0.10, rely=0.10)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrDatos, width=400, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.30, rely=0.10)
        self.TxtCodigo.bind("<KeyRelease>", self.Consulta_Prestamos)
        
        # Treeview
        self.Tree = ttk.Treeview(self.FrDatos, columns=('USUARIO', 'NOMBRE', 'TITULO', 'FECHA_PRESTAMO', 'FECHA_DEVOLUCION'))
        
        # Configurar los headings
        self.Tree.heading("#0", text="")
        self.Tree.heading("USUARIO", text="Usuario")
        self.Tree.heading("NOMBRE", text="Nombre")
        self.Tree.heading("TITULO", text="Titulo")
        self.Tree.heading("FECHA_PRESTAMO", text="Fecha Prestamo")
        self.Tree.heading("FECHA_DEVOLUCION", text="Fecha Devolucion")

        # Configurar la columna
        self.Tree.column("#0", width=0)
        self.Tree.column("USUARIO", width=100)
        self.Tree.column("NOMBRE", width=140)
        self.Tree.column("TITULO", width=150)
        self.Tree.column("FECHA_PRESTAMO", width=140)
        self.Tree.column("FECHA_DEVOLUCION", width=140)
        
        # Posicionar el Tree
        self.Tree.place(relx=0.08, rely=0.28)
        
        # Cargar Datos
        conexion.Cargar_Prestamos(self.Tree)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.24)
    def Create_Add(self):
        self.delete_frdatos()
        # Cambiar Botones
        self.BtnRegistrar.configure(image=self.Inicio, text='Inicio', command=self.Home_Prestamos)
        if (self.BtnConsultar.cget('image') == self.Inicio):
            self.BtnConsultar.configure(image=self.Consultar, text='Consultar', command=self.Create_Search)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrDatos, text='Codigo', fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', width=280, anchor='w')
        self.LblCodigo.place(relx=0.20, rely=0.10)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.40, rely=0.10)
        
        # Label Nombre
        self.LblNombre = ctk.CTkLabel(self.FrDatos, text='Nombre', fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', width=280, anchor='w')
        self.LblNombre.place(relx=0.20, rely=0.20)
        
        # Entry Nombre
        self.TxtNombre = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtNombre.place(relx=0.40, rely=0.20)
        
        # Label Telefono
        self.LblFechaPrestamo = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', text='Fecha prestamo', text_color='#FFFFFF', font=('Roboto', 18), anchor='w')
        self.LblFechaPrestamo.place(relx=0.20, rely=0.30)
        
        # Entry Telefono
        self.TxtFechaPrestamo = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtFechaPrestamo.place(relx=0.40, rely=0.30)

        # Label Ficha
        self.LblFechaDevolucion = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', text='Fecha Devolucion', anchor='w')
        self.LblFechaDevolucion.place(relx=0.20, rely=0.40)
        
        # Entry Ficha
        self.TxtFechaDevolucion = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', font=('Roboto', 18), text_color='#000000')
        self.TxtFechaDevolucion.place(relx=0.40, rely=0.40)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.52)
        
        # Combobox Items
        libros = conexion.Obtener_Libros()
        self.CbItems = ctk.CTkComboBox(self.FrDatos, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18),  width=320, button_color='#f09641', values=libros, state='readonly')
        self.CbItems.place(relx=0.29, rely=0.62)
        
        # Btn Guardar
        self.BtnGuardar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Guardar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Guardar, hover=True, hover_color='#002029', command=self.Guardar_Prestamo)
        self.BtnGuardar.place(relx=0.25, rely=0.72)
        
        # Btn Cancelar
        self.BtnCancelar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Cancelar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Cancelar, hover=True, hover_color='#002029', command=self.Cancelar_Prestamo)
        self.BtnCancelar.place(relx=0.50, rely=0.72)
    def Create_Search_Devoluciones(self):
        self.delete_frdatos()
        # Cambiar Boton
        self.BtnConsultar.configure(image=self.Inicio, text='Inicio', command=self.Home_Devoluciones)
        if (self.BtnRegistrar.cget('image') == self.Inicio):
            self.BtnRegistrar.configure(image=self.Registrar, text='Registrar', command=self.Create_Add_Devoluciones)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrDatos, width=120, font=('Roboto', 18), text='Ingrese el codigo:')
        self.LblCodigo.place(relx=0.10, rely=0.10)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrDatos, width=400, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.30, rely=0.10)
        self.TxtCodigo.bind("<KeyRelease>", self.Consulta_Devoluciones)
        
        # Treeview
        self.Tree = ttk.Treeview(self.FrDatos, columns=('USUARIO', 'NOMBRE', 'TITULO', 'FECHA_DEVOLUCION', 'FECHA_DEVOLUCION_REAL'))
        
        # Configurar los headings
        self.Tree.heading("#0", text="")
        self.Tree.heading("USUARIO", text="Usuario")
        self.Tree.heading("NOMBRE", text="Nombre")
        self.Tree.heading("TITULO", text="Titulo")
        self.Tree.heading("FECHA_DEVOLUCION", text="Fecha Devolucion")
        self.Tree.heading("FECHA_DEVOLUCION_REAL", text="Fecha Devolucion Real")

        # Configurar la columna
        self.Tree.column("#0", width=0)
        self.Tree.column("USUARIO", width=100)
        self.Tree.column("NOMBRE", width=150)
        self.Tree.column("TITULO", width=140)
        self.Tree.column("FECHA_DEVOLUCION", width=120)
        self.Tree.column("FECHA_DEVOLUCION_REAL", width=160)
        
        # Posicionar el Tree
        self.Tree.place(relx=0.08, rely=0.28)
        
        # Cargar Datos
        conexion.Cargar_Devoluciones(self.Tree)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.24)
    def Create_Add_Devoluciones(self):
        self.delete_frdatos()
        # Cambiar Botones
        self.BtnRegistrar.configure(image=self.Inicio, text='Inicio', command=self.Home_Devoluciones)
        if (self.BtnConsultar.cget('image') == self.Inicio):
            self.BtnConsultar.configure(image=self.Consultar, text='Consultar', command=self.Create_Search_Devoluciones)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrDatos, text='Codigo', fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', width=280, anchor='w')
        self.LblCodigo.place(relx=0.20, rely=0.10)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.40, rely=0.10)
        self.TxtCodigo.bind("<FocusOut>", self.Cargar_Prestamos)
        
        # Label Nombre
        self.LblNombre = ctk.CTkLabel(self.FrDatos, text='Nombre', fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', width=280, anchor='w')
        self.LblNombre.place(relx=0.20, rely=0.20)
        
        # Entry Nombre
        self.TxtNombre = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtNombre.place(relx=0.40, rely=0.20)
        
        # Label Fecha Devolucion
        self.LblFechaDevolucion = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', text='Fecha Devolucion', text_color='#FFFFFF', font=('Roboto', 18), anchor='w')
        self.LblFechaDevolucion.place(relx=0.20, rely=0.30)
        
        # Entry Fecha Devolucion
        self.TxtFechaDevolucion = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtFechaDevolucion.place(relx=0.40, rely=0.30)

        # Label Ficha
        self.LblFechaDevolucionReal = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', text='Fecha Real', anchor='w')
        self.LblFechaDevolucionReal.place(relx=0.20, rely=0.40)
        
        # Entry Ficha
        self.TxtFechaDevolucionReal = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', font=('Roboto', 18), text_color='#000000')
        self.TxtFechaDevolucionReal.place(relx=0.40, rely=0.40)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.52)
        
        # Combobox Items
        self.CbItems = ctk.CTkComboBox(self.FrDatos, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18),  width=320, button_color='#f09641', state='readonly')
        self.CbItems.place(relx=0.29, rely=0.62)
        
        # Btn Guardar
        self.BtnGuardar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Guardar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Guardar, hover=True, hover_color='#002029', command=self.Guardar_Devolucion)
        self.BtnGuardar.place(relx=0.25, rely=0.72)
        
        # Btn Cancelar
        self.BtnCancelar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Cancelar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Cancelar, hover=True, hover_color='#002029', command=self.Cancelar_Devolucion)
        self.BtnCancelar.place(relx=0.50, rely=0.72)
    def Agregar_Sancion(self):
        Sanctions_window = tk.Toplevel(self.FrSanctions)
        Sanctions_window.title("Agregar Nueva Sancion")
        Sanctions_window.config(bg="#002029")
    
        screen_width = Sanctions_window.winfo_screenwidth()
        screen_height = Sanctions_window.winfo_screenheight()
        window_width = 400
        window_height = 300

        position_top = int((screen_height / 2) - (window_height / 2))
        position_left = int((screen_width / 2) - (window_width / 2))

        Sanctions_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        Sanctions_window.resizable(False, False)
    
        LblMulta = tk.Label(Sanctions_window, text="Id Multa", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        LblMulta.place(relx=0.05, rely=0.10)
        self.TxtMulta = tk.Entry(Sanctions_window, font=("Roboto", 12))
        self.TxtMulta.place(relx=0.35, rely=0.10)

        LblUsuario = tk.Label(Sanctions_window, text="Id Usuario", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        LblUsuario.place(relx=0.05, rely=0.25)
        self.TxtUsuario = tk.Entry(Sanctions_window, font=("Roboto", 12))
        self.TxtUsuario.place(relx=0.35, rely=0.25)

        Lbl_Monto = tk.Label(Sanctions_window, text="Monto", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        Lbl_Monto.place(relx=0.05, rely=0.40)
        self.TxtMonto = tk.Entry(Sanctions_window, font=("Roboto", 12))
        self.TxtMonto.place(relx=0.35, rely=0.40)

        LblFecha = tk.Label(Sanctions_window, text="Fecha", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        LblFecha.place(relx=0.05, rely=0.55)
        self.TxtFecha = tk.Entry(Sanctions_window, font=("Roboto", 12))
        self.TxtFecha.place(relx=0.35, rely=0.55)

        save_button = tk.Button(Sanctions_window, text="Guardar", font=("Roboto", 12), bg="#005066", fg="#FFFFFF", command=self.Guardar_Sancion)
        save_button.place(relx=0.25, rely=0.70)
    
        cancel_button = tk.Button(Sanctions_window, text="Cancelar", font=("Roboto", 12), bg="#D32F2F", fg="#FFFFFF", command=Sanctions_window.destroy)
        cancel_button.place(relx=0.45, rely=0.70)

        Sanctions_window.transient(self.FrSanctions)
        Sanctions_window.grab_set()

    # Commands
    def Home_Prestamos(self):
        self.Loans_Form()
    def Home_Devoluciones(self):
        self.Returns_Form()
    def Cerrar_Sesion(self):
        # Confirmar si el usuario realmente desea cerrar sesión
        respuesta = mb.askyesno("Cerrar sesión", "¿Estás seguro de que quieres cerrar sesión?")
        if respuesta:
            self.FrmMenu.destroy()
            login.Start()
    
    # Guardar
    def Agregar_Registro(self):
        add_window = tk.Toplevel(self.FrInventory)
        add_window.title("Agregar Nuevo Registro")
        add_window.config(bg="#002029")
    
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()
        window_width = 400
        window_height = 450

        position_top = int((screen_height / 2) - (window_height / 2))
        position_left = int((screen_width / 2) - (window_width / 2))

        add_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        add_window.resizable(False, False)
    
        label_codigo = tk.Label(add_window, text="Código", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_codigo.place(relx=0.05, rely=0.10)
        self.TxtCodigoAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtCodigoAdd.place(relx=0.35, rely=0.10)

        label_titulo = tk.Label(add_window, text="Titulo", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_titulo.place(relx=0.05, rely=0.20)
        self.TxtTituloAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtTituloAdd.place(relx=0.35, rely=0.20)

        label_autor = tk.Label(add_window, text="Autor", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_autor.place(relx=0.05, rely=0.30)
        self.TxtAutorAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtAutorAdd.place(relx=0.35, rely=0.30)

        label_Editorial = tk.Label(add_window, text="Editorial", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_Editorial.place(relx=0.05, rely=0.40)
        self.TxtEditorialAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtEditorialAdd.place(relx=0.35, rely=0.40)

        label_categoria = tk.Label(add_window, text="Categoría", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_categoria.place(relx=0.05, rely=0.50)
        self.CbItemsAdd = ttk.Combobox(add_window, values=["Distopía", "Clásico", "Misterio", "Romance"], font=("Roboto", 12))
        self.CbItemsAdd.place(relx=0.35, rely=0.50)
    
        label_estado = tk.Label(add_window, text="Estado", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_estado.place(relx=0.05, rely=0.60)
        self.CbEstadoAdd = ttk.Combobox(add_window, values=["Disponible", "No disponible"], font=("Roboto", 12))
        self.CbEstadoAdd.place(relx=0.35, rely=0.60)

        save_button = tk.Button(add_window, text="Guardar", font=("Roboto", 12), bg="#005066", fg="#FFFFFF", command=self.Guardar_Registro)
        save_button.place(relx=0.25, rely=0.70)
    
        cancel_button = tk.Button(add_window, text="Cancelar", font=("Roboto", 12), bg="#D32F2F", fg="#FFFFFF", command=add_window.destroy)
        cancel_button.place(relx=0.45, rely=0.70)

        add_window.transient(self.FrInventory)
        add_window.grab_set()
    def Guardar_Registro(self):
        codigo = self.TxtCodigoAdd.get()
        titulo = self.TxtTituloAdd.get()
        autor = self.TxtAutorAdd.get()
        editorial = self.TxtEditorialAdd.get()
        categoria = self.CbItemsAdd.get()
        estado = self.CbEstadoAdd.get()
    
        if not codigo or not titulo or not autor or not editorial or not categoria or not estado:
            mb.showwarning(title="Por favor complete todos los campos", message="Los campos no pueden estar vacios")
            return
        
        conexion.Insertar_Datos(codigo, titulo, autor, editorial, categoria, estado)
        mb.showinfo(title='Guardado Exitoso', message='El prestamo se ha guardado correctamente')
    
        self.TxtCodigoAdd.delete(0, tk.END)
        self.TxtTituloAdd.delete(0, tk.END)
        self.TxtAutorAdd.delete(0, tk.END)
        self.TxtEditorialAdd.delete(0, tk.END)
        self.CbItemsAdd.set('')
        self.CbEstadoAdd.set('')

        self.Inventory_Panel()
    def Guardar_Prestamo(self):
        try:
            codigo = self.TxtCodigo.get()
            nombre = self.TxtNombre.get()
            titulo = self.CbItems.get()
            fecha_prestamo = self.TxtFechaPrestamo.get()
            fecha_devolucion = self.TxtFechaDevolucion.get()
        
            if not codigo or not nombre or not titulo or not fecha_prestamo or not fecha_devolucion:
                mb.showwarning(title="Campos vacios", message="Los campos no pueden estar vacios")
                return

            conexion.Insertar_Prestamos(codigo, nombre, titulo, fecha_prestamo, fecha_devolucion)
            mb.showinfo(title='Guardado exitoso', message='El prestamo se ha guardado correctamente')
        
            self.TxtCodigo.delete(0, tk.END)
            self.TxtNombre.delete(0, tk.END)
            self.CbItems.set('')
            self.TxtFechaPrestamo.delete(0, tk.END)
            self.TxtFechaDevolucion.delete(0, tk.END)
        except Exception as e:
            print(f"Error al guardar el registro: {e}")
            mb.showerror(title='Error', message='Hubo un error al guardar el registro')
    def Guardar_Devolucion(self):
        try:
            codigo = self.TxtCodigo.get()
            nombre = self.TxtNombre.get()
            titulo = self.CbItems.get()
            fecha_devolucion = self.TxtFechaDevolucion.get()
            fecha_devolucion_real = self.TxtFechaDevolucionReal.get()
        
            if not codigo or not nombre or not titulo or not fecha_devolucion or not fecha_devolucion_real:
                mb.showwarning(title="Campos vacios", message="Los campos no pueden estar vacios")
                return
            
            respuesta = mb.askyesno(title='Confirmar Devolucion', message='¿Estás seguro de que quieres confirmar la devolucion?')
            if respuesta:
                try:
                    conexion.Insertar_Devolucion(codigo, nombre, titulo, fecha_devolucion, fecha_devolucion_real)
                    conexion.Eliminar_Prestamo(codigo)
                    mb.showinfo(title='Guardado exitoso', message='La devolucion se ha guardado correctamente')
                except Exception as e:
                    print(f"Error al registrar la devolución o eliminar el préstamo: {e}")
                    mb.showerror(title='Error', message='Hubo un problema al registrar la devolución o al eliminar el préstamo')
        
            self.TxtCodigo.delete(0, tk.END)
            self.TxtNombre.delete(0, tk.END)
            self.CbItems.set('')
            self.TxtFechaDevolucion.delete(0, tk.END)
            self.TxtFechaDevolucionReal.delete(0, tk.END)
        except Exception as e:
            print(f"Error al guardar el registro: {e}")
            mb.showerror(title='Error', message='Hubo un error al guardar el registro')
    def Guardar_Sancion(self):
        try:
            codigo = self.TxtMulta.get()
            usuario = self.TxtUsuario.get()
            monto = self.TxtMonto.get()
            fecha = self.TxtFecha.get()
        
            if not codigo or not usuario or not monto or not fecha:
                mb.showwarning(title="Campos vacios", message="Los campos no pueden estar vacios")
                return
            
            respuesta = mb.askyesno(title='Confirmar Devolucion', message='¿Estás seguro de que quieres confirmar la sancion?')
            if respuesta:
                try:
                    conexion.Insertar_Sancion(codigo, usuario, monto, fecha)
                    mb.showinfo(title='Guardado exitoso', message='La sancion se ha guardado correctamente')
                except Exception as e:
                    print(f"Error al registrar la sancion: {e}")
                    mb.showerror(title='Error', message='Hubo un problema al registrar la sancion')
        
            self.TxtMulta.delete(0, tk.END)
            self.TxtUsuario.delete(0, tk.END)
            self.TxtMonto.delete(0, tk.END)
            self.TxtFecha.delete(0, tk.END)
            self.Sanctions_Form()
            
        except Exception as e:
            print(f"Error al guardar la sancion: {e}")
            mb.showerror(title='Error', message='Hubo un error al guardar el registro')
        
    # Eliminar
    def Eliminar_Registro(self):
        selected_item = self.Tree.selection()

        if not selected_item:
            mb.showwarning("Selección vacía", "Por favor, selecciona un registro para eliminar.")
            return

        item_values = self.Tree.item(selected_item)['values']
    
        isbn = item_values[0]
        confirm = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el registro con ISBN: {isbn}?")

        if confirm:
            try:
                conexion.Eliminar_Datos(isbn)
                self.Tree.delete(selected_item)
                mb.showinfo("Eliminación exitosa", f"El registro con ISBN {isbn} ha sido eliminado.")
        
            except Exception as e:
                mb.showerror("Error", f"Hubo un error al intentar eliminar el registro: {e}")
    def Eliminar_Sanciones(self):
        selected_item = self.Tree.selection()

        if not selected_item:
            mb.showwarning("Selección vacía", "Por favor, selecciona un registro para eliminar.")
            return

        item_values = self.Tree.item(selected_item)['values']
    
        codigo = item_values[1]
        confirm = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el registro con Codigo: {codigo}?")

        if confirm:
            try:
                conexion.Eliminar_Sancion(codigo)
                self.Tree.delete(selected_item)
                mb.showinfo("Eliminación exitosa", f"El registro con Codigo {codigo} ha sido eliminado.")
        
            except Exception as e:
                mb.showerror("Error", f"Hubo un error al intentar eliminar el registro: {e}")
    
    # Consultar
    def Consulta_Libros(self, event):
        search_text = self.TxtConsulta.get().lower()
    
        for item in self.Tree.get_children():
            self.Tree.delete(item)
    
        all_data = conexion.Obtener_Datos()
    
        filtered_data = []
        for record in all_data:
            if any(search_text in str(field).lower() for field in record):
                filtered_data.append(record)
        
        for record in filtered_data:
            self.Tree.insert("", "end", values=record)
    def Consulta_Prestamos(self, event):
        search_text = self.TxtCodigo.get().lower()
    
        for item in self.Tree.get_children():
            self.Tree.delete(item)
    
        all_data = conexion.Consulta_Prestamos()
    
        filtered_data = []
        for record in all_data:
            if any(search_text in str(field).lower() for field in record):
                filtered_data.append(record)
        
        for record in filtered_data:
            self.Tree.insert("", "end", values=record)
    def Consulta_Devoluciones(self, event):
        search_text = self.TxtCodigo.get().lower()
    
        for item in self.Tree.get_children():
            self.Tree.delete(item)
    
        all_data = conexion.Consulta_Devoluciones()
    
        filtered_data = []
        for record in all_data:
            if any(search_text in str(field).lower() for field in record):
                filtered_data.append(record)
        
        for record in filtered_data:
            self.Tree.insert("", "end", values=record)
    def Consulta_Sanciones(self, event):
        search_text = self.TxtCodigo.get().lower()
    
        for item in self.Tree.get_children():
            self.Tree.delete(item)
    
        all_data = conexion.Consulta_Sanciones()
    
        filtered_data = []
        for record in all_data:
            if any(search_text in str(field).lower() for field in record):
                filtered_data.append(record)
        
        for record in filtered_data:
            self.Tree.insert("", "end", values=record)
    
    # Comandos
    def Cargar_Prestamos(self, event):
        user_id = self.TxtCodigo.get()

        if user_id:
            libros_prestados = conexion.Obtener_Prestamos(user_id)
            titulos_libros = [libro[2] for libro in libros_prestados]
            self.CbItems.configure(values=titulos_libros)
    def Cancelar_Prestamo(self):
        respuesta = mb.askyesno(title='Cancelar', message='¿Estás seguro de que quieres cancelar?')
        if respuesta:
            self.TxtCodigo.delete(0, tk.END)
            self.TxtNombre.delete(0, tk.END)
            self.TxtFechaPrestamo.delete(0, tk.END)
            self.TxtFechaDevolucion.delete(0, tk.END)
            self.CbItems.set('')
            self.Home_Prestamos()
    def Cancelar_Devolucion(self):
        respuesta = mb.askyesno(title='Cancelar', message='¿Estás seguro de que quieres cancelar?')
        if respuesta:
            self.TxtCodigo.delete(0, tk.END)
            self.TxtNombre.delete(0, tk.END)
            self.TxtFechaDevolucion.delete(0, tk.END)
            self.TxtFechaDevolucionReal.delete(0, tk.END)
            self.CbItems.set('')
            self.Home_Devoluciones()
    
    # Indicadores
    def Hide_Indicators(self):
        self.IndInventario.configure(bg='#005066')
        self.IndPrestamos.configure(bg='#005066')
        self.IndDevoluciones.configure(bg='#005066')
        self.IndSanciones.configure(bg='#005066')
    def Indicators(self, lb, page):
        self.Hide_Indicators()
        lb.configure(bg='#FFFFFF')
        self.delete_frames()
        page()

    # Controlarores
    def delete_frames(self):
        for frame in self.FrPages.winfo_children():
            frame.destroy()  
    def delete_frdatos(self):
        for frame in self.FrDatos.winfo_children():
            frame.destroy()
    
    # Controles
    def Controles_Panel_Lateral(self):
        # Label Foto
        self.LblProfile = ctk.CTkLabel(self.FrNav, bg_color='#005066', text='', image=self.Foto)
        self.LblProfile.place(relx=0.18, rely=0.05)
        
        # Btn Inventario
        self.IndInventario = tk.Label(self.FrNav, background='#005066', width=5, height=3, text='')
        self.IndInventario.place(relx=0.97, rely=0.40)
        
        self.BtnInventario = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Inventario', image=self.Inventario, width=193,  height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=lambda: self.Indicators(self.IndInventario, self.Inventory_Panel))
        self.BtnInventario.place(relx=0, rely=0.40)
        
        # Btn Prestamos
        self.IndPrestamos = tk.Label(self.FrNav, background='#005066', width=5, height=3, text='')
        self.IndPrestamos.place(relx=0.97, rely=0.49)
        
        self.BtnPrestamos = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Prestamos', image=self.Prestamos, width=193, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=lambda:self.Indicators(self.IndPrestamos, self.Loans_Form))
        self.BtnPrestamos.place(relx=0, rely=0.49)
        
        # Btn Devoluciones
        self.IndDevoluciones = tk.Label(self.FrNav, background='#005066', width=5, height=3, text='')
        self.IndDevoluciones.place(relx=0.97, rely=0.58)
        
        self.BtnDevoluciones = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Devoluciones', image=self.Devoluciones, width=193, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=lambda:self.Indicators(self.IndDevoluciones, self.Returns_Form))
        self.BtnDevoluciones.place(relx=0, rely=0.58)
        
        # Btn Sanciones
        self.IndSanciones = tk.Label(self.FrNav, background='#005066', width=5, height=3, text='')
        self.IndSanciones.place(relx=0.97, rely=0.67)
        
        self.BtnSanciones = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Sanciones', image=self.Sanciones, width=193, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=lambda:self.Indicators(self.IndSanciones, self.Sanctions_Form))
        self.BtnSanciones.place(relx=0, rely=0.67)
        
        # Btn Salir
        self.BtnSalir = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Cerrar Sesion', image=self.Salir, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=self.Cerrar_Sesion)
        self.BtnSalir.place(relx=0, rely=0.92)
def Start():
    App()