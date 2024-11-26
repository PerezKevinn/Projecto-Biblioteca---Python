import tkinter as tk
import customtkinter as ctk
import tooltip
from PIL import Image
from tkinter import ttk

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
        SpSalir = Image.open('img/icon/exit.png')
        
        # Variables Inventario
        SpLibros = Image.open('img/icon/libros.png')
        SpEquipos = Image.open('img/icon/laptop.png')
        SpNuevo = Image.open('img/icon/add.png')
        SpEditar = Image.open('img/icon/update.png')
        SpEliminar = Image.open('img/icon/delete.png')
        SpBuscar = Image.open('img/icon/search.png')
        
        # Imagenes
        self.Foto = ctk.CTkImage(light_image=SpFoto, dark_image=SpFoto, size=(128,128))
        self.Inventario = ctk.CTkImage(light_image=SpInventario, dark_image=SpInventario, size=(32,32))
        self.Prestamos = ctk.CTkImage(light_image=SpPrestamos, dark_image=SpPrestamos, size=(32,32))
        self.Devoluciones = ctk.CTkImage(light_image=SpDevoluciones, dark_image=SpDevoluciones, size=(32,32))
        self.Sanciones = ctk.CTkImage(light_image=SpSanciones, dark_image=SpSanciones, size=(32,32))
        self.Salir = ctk.CTkImage(light_image=SpSalir, dark_image=SpSalir, size=(32,32))
        
        # Imagenes Botones Inventario
        self.Libros = ctk.CTkImage(light_image=SpLibros, dark_image=SpLibros, size=(32,32))
        self.Equipos = ctk.CTkImage(light_image=SpEquipos, dark_image=SpEquipos, size=(32,32))
        self.Nuevo = ctk.CTkImage(light_image=SpNuevo, dark_image=SpNuevo, size=(32,32))
        self.Editar = ctk.CTkImage(light_image=SpEditar, dark_image=SpEditar, size=(32,32))
        self.Eliminar = ctk.CTkImage(light_image=SpEliminar, dark_image=SpEliminar, size=(32,32))
        self.Buscar = ctk.CTkImage(light_image=SpBuscar, dark_image=SpBuscar, size=(32,32))
        
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
        
        # Frame Grilla
        self.FrGrilla = ctk.CTkFrame(self.FrInventory, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrGrilla.place(relx=0.05, rely=0.20)
              
        # Grilla de Consulta
        self.Grid = ttk.Treeview(self.FrGrilla, columns=5, height=21)
        self.Grid.place(relx=0.10, rely=0.05)
        # Definicion de Columnas
        self.Grid['columns'] = ('ISBN', 'Titulo', 'Categoria', 'Autor', 'Estado')   
        # Formato de las columnas
        self.Grid.column('#0', width=1, minwidth=1, anchor='center')
        self.Grid.column('ISBN', width=50, minwidth=25, anchor='center')
        self.Grid.column('Titulo', width=200, minwidth=25, anchor='center')
        self.Grid.column('Categoria', width=80, minwidth=25, anchor='center')
        self.Grid.column('Autor', width=180, minwidth=25, anchor='center')
        self.Grid.column('Estado', width=80, minwidth=25, anchor='center')
        # Encabezados
        self.Grid.heading('#0', text='', anchor='center')
        self.Grid.heading('ISBN', text='Codigo', anchor='center')
        self.Grid.heading('Titulo', text='Titulo', anchor='center')
        self.Grid.heading('Categoria', text='Categoria', anchor='center')
        self.Grid.heading('Autor', text='Autor', anchor='center')
        self.Grid.heading('Estado', text='Estado', anchor='center')
        # Insertar Datos
        self.Grid.insert(parent='', index='end', iid=0, text='', values=('00001', 'Cien años de soledad', 'Literatura', 'Gabriel Garcia Marquez', 'Disponible'))
        
        # CRUD
        self.BtnNuevo = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Nuevo, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF')
        self.BtnNuevo.place(relx=0.88, rely=0.10)
        tooltip.Hovertip(self.BtnNuevo, text='Agregar nuevo registro', hover_delay=100)
        
        self.BtnEditar = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Editar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF')
        self.BtnEditar.place(relx=0.88, rely=0.22)
        tooltip.Hovertip(self.BtnEditar, text='Editar registro seleccionado', hover_delay=100)
        
        self.BtnEliminar = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Eliminar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF')
        self.BtnEliminar.place(relx=0.88, rely=0.34)
        tooltip.Hovertip(self.BtnEliminar, text='Eliminar registro seleccionado', hover_delay=100)
        
        self.BtnBuscar = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Buscar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF')
        self.BtnBuscar.place(relx=0.88, rely=0.46)
        tooltip.Hovertip(self.BtnBuscar, text='Buscar registro', hover_delay=100)
        
        # Btn Libros
        self.BtnLibros = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Libros, text='Libros', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029')
        self.BtnLibros.place(relx=0.25, rely=0.18)
        
        # Btn Equipos
        self.BtnEquipos = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Equipos, text='Equipos', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029')
        self.BtnEquipos.place(relx=0.50, rely=0.18)
    def Loans_Form(self):
        
        # Frame Prestamos
        self.FrLoans = tk.Frame(self.FrPages, background='#002029', width=900, height=800)
        self.FrLoans.place(relx=0.05, rely=0)
        self.FrLoans.grid_propagate(False)
        
    def Returns_Form(self):
        pass
    def Sanctions_Form(self):
        pass
    
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
    
    # Controlar Frames
    def delete_frames(self):
        for frame in self.FrPages.winfo_children():
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
        self.BtnSalir = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Cerrar Sesion', image=self.Salir, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False)
        self.BtnSalir.place(relx=0, rely=0.92)
App()