import tkinter as tk
import customtkinter as ctk
import tooltip
import login
from tkinter import messagebox as mb
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
        
        # Frame Grilla
        self.FrGrilla = ctk.CTkFrame(self.FrInventory, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrGrilla.place(relx=0.05, rely=0.20)
              
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
        self.BtnConsultar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Consultar, text='Consultar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Search)
        self.BtnConsultar.place(relx=0.25, rely=0.18)
        
        # Btn Registrar
        self.BtnRegistrar = ctk.CTkButton(self.FrButtons, width=150, height=80, image=self.Registrar, text='Registrar', fg_color='#005066', text_color='#FFFFFF', compound='left', font=('Roboto', 18, 'bold'), border_width=1, border_color='#FFFFFF', hover=True, hover_color='#002029', command=self.Create_Add)
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
    def Information_Form(self):
        
    # Frames
    def Create_Search(self):
        self.delete_frdatos()
        # Cambiar Boton
        self.BtnConsultar.configure(image=self.Inicio, text='Inicio', command=self.Home)
        if (self.BtnRegistrar.cget('image') == self.Inicio):
            self.BtnRegistrar.configure(image=self.Registrar, text='Registrar', command=self.Create_Add)
        
        # Label Codigo
        self.LblCodigo = ctk.CTkLabel(self.FrDatos, width=120, font=('Roboto', 18), text='Ingrese el codigo:')
        self.LblCodigo.place(relx=0.10, rely=0.10)
        
        # Entry Codigo
        self.TxtCodigo = ctk.CTkEntry(self.FrDatos, width=400, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtCodigo.place(relx=0.30, rely=0.10)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.27)
    def Create_Add(self):
        self.delete_frdatos()
        # Cambiar Botones
        self.BtnRegistrar.configure(image=self.Inicio, text='Inicio', command=self.Home)
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
        self.LblTel = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', text='Telefono', text_color='#FFFFFF', font=('Roboto', 18), anchor='w')
        self.LblTel.place(relx=0.20, rely=0.30)
        
        # Entry Telefono
        self.TxtTel = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18))
        self.TxtTel.place(relx=0.40, rely=0.30)

        # Label Ficha
        self.LblFicha = ctk.CTkLabel(self.FrDatos, width=280, fg_color='#005066', font=('Roboto', 18), text_color='#FFFFFF', text='Ficha', anchor='w')
        self.LblFicha.place(relx=0.20, rely=0.40)
        
        # Entry Ficha
        self.TxtFicha = ctk.CTkEntry(self.FrDatos, width=280, fg_color='#FFFFFF', font=('Roboto', 18), text_color='#000000')
        self.TxtFicha.place(relx=0.40, rely=0.40)
        
        # Separador
        self.Separador = ctk.CTkLabel(self.FrDatos, width=670, fg_color='#FFFFFF', text='', font=('Roboto', 2), height=2)
        self.Separador.place(relx=0.08, rely=0.52)
        
        # Combobox Items
        self.CbItems = ctk.CTkComboBox(self.FrDatos, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18),  width=320, button_color='#f09641')
        self.CbItems.place(relx=0.29, rely=0.62)
        
        # Btn Guardar
        self.BtnGuardar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Guardar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Guardar, hover=True, hover_color='#002029')
        self.BtnGuardar.place(relx=0.25, rely=0.72)
        
        # Btn Cancelar
        self.BtnCancelar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Cancelar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Cancelar, hover=True, hover_color='#002029')
        self.BtnCancelar.place(relx=0.50, rely=0.72)

    # Commands
    def Home(self):
        self.Loans_Form()
            
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
        
        # Btn Information
        self.IndInformation = tk.Label(self.FrNav, background='#005066', width=5, height=3, text='')
        self.IndInformation.place(relx=0.97, rely=0.67)
        
        self.BtnInformation = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Informes', image=self.Informes, width=193, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False, command=lambda:self.Indicators(self.IndInformation, self.Information_Form))
        self.BtnInformation.place(relx=0, rely=0.76)
        
        # Btn Salir
        self.BtnSalir = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Cerrar Sesion', image=self.Salir, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False)
        self.BtnSalir.place(relx=0, rely=0.92)
def Start():
    App()