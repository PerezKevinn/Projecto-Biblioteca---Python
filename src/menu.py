import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

class App():
    def __init__(self):
        
        # Ventana Principal
        self.FrmMenu = tk.Tk()
        self.FrmMenu.title("Menu Principal")
        self.FrmMenu.config(background='#002029')
        self.FrmMenu.resizable(False,False)
        
        # Imagenes
        self.SpFoto = tk.PhotoImage(file='img/pic/profile.png')
        self.SpInventario = tk.PhotoImage(file='img/icon/inventory.png')
        self.SpPrestamos = tk.PhotoImage(file='img/icon/loans.png')
        self.SpDevoluciones = tk.PhotoImage(file='img/icon/return.png')
        self.SpSanciones = tk.PhotoImage(file='img/icon/sanctions.png')
        self.SpSalir = tk.PhotoImage(file='img/icon/exit.png')
        
        # Imagenes Inventario
        self.SpLibros = tk.PhotoImage(file='img/icon/libros.png')
        self.SpEquipos = tk.PhotoImage(file='img/icon/laptop.png')
        
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
    
    def Paneles(self):
        # Menu lateral
        self.FrNav = ctk.CTkFrame(self.FrmMenu, width=200, height=600, fg_color='#005066', corner_radius=0)
        self.FrNav.pack(side=ctk.LEFT)
    
    # Formulario de Inventario
    def Inventory_Panel(self):
        # Frame de Inventario
        self.FrInventory = tk.Frame(self.FrmMenu, background='#002029', width=900, height=800)
        self.FrInventory.pack(pady=20)
        self.FrInventory.grid_propagate(False)
        
        # Frame Botones
        self.FrButtons = ctk.CTkFrame(self.FrInventory, width=800, height=120, corner_radius=30, fg_color='#005066')
        self.FrButtons.place(relx=0.05, rely=0.05)
        
        # Frame Grilla
        self.FrGrilla = ctk.CTkFrame(self.FrInventory, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrGrilla.place(relx=0.05, rely=0.25)
        
        # Grilla de Consulta
        self.Grid = ttk.Treeview(self.FrGrilla, columns=5, height=21)
        self.Grid.place(relx=0.05, rely=0.05)
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
        # Posicionamiento de la grilla
        self.Grid.place(relx=0.10, rely=0.05)
        
        # Btn Libros
        self.BtnLibros = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.SpLibros, text='Libros', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029')
        self.BtnLibros.place(relx=0.25, rely=0.18)
        
        # Btn Equipos
        self.BtnEquipos = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.SpEquipos, text='Equipos', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029')
        self.BtnEquipos.place(relx=0.50, rely=0.18)
        
    def Controles_Panel_Lateral(self):
        # Label Foto
        self.LblProfile = ctk.CTkLabel(self.FrNav, bg_color='#005066', text='', image=self.SpFoto)
        self.LblProfile.pack(side=ctk.TOP, pady=(20,10))
        
        # Btn Inventario
        self.BtnInventario = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Inventario', image=self.SpInventario, width=250,  height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=True, hover_color='#002029', command=self.Inventory_Panel)
        self.BtnInventario.pack(side=ctk.TOP, pady=(90, 0))
        
        # Btn Prestamos
        self.BtnPrestamos = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Prestamos', image=self.SpPrestamos, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=True, hover_color='#002029')
        self.BtnPrestamos.pack(side=ctk.TOP)
        
        # Btn Devoluciones
        self.BtnDevoluciones = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Devoluciones', image=self.SpDevoluciones, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=True, hover_color='#002029')
        self.BtnDevoluciones.pack(side=ctk.TOP)
        
        # Btn Sanciones
        self.BtnSanciones = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Sanciones', image=self.SpSanciones, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=True, hover_color='#002029')
        self.BtnSanciones.pack(side=ctk.TOP)
        
        # Btn Salir
        self.BtnSalir = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Cerrar Sesion', image=self.SpSalir, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=True, hover_color='#002029')
        self.BtnSalir.pack(side=ctk.BOTTOM, pady=(180, 0))
App()