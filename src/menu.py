import tkinter as tk
import customtkinter as ctk
import tooltip
import conexion
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
        
        # Configurar el evento de cambio de texto en TxtConsulta
        self.TxtConsulta.bind("<KeyRelease>", self.consultar_dinamicamente)
        
        # Frame Grilla
        self.FrGrilla = ctk.CTkFrame(self.FrInventory, width=800, height=500, corner_radius=30, fg_color='#005066')
        self.FrGrilla.place(relx=0.05, rely=0.20)
        
        # Treeview
        self.Tree = ttk.Treeview(self.FrGrilla, columns=('ISBN', 'Titulo', 'Autor', 'Editorial', 'Categoria', 'Estado', 'Fecha_Ingreso'))
        
        # Configurar los headings
        self.Tree.heading("#0", text="")
        self.Tree.heading("ISBN", text="ISBN")
        self.Tree.heading("Titulo", text="Título")
        self.Tree.heading("Autor", text="Autor")
        self.Tree.heading("Editorial", text="Editorial")
        self.Tree.heading("Categoria", text="Categoría")
        self.Tree.heading("Estado", text="Estado")
        self.Tree.heading("Fecha_Ingreso", text="Fecha Ingreso")
        
        # Configurar la columna
        self.Tree.column("#0", width=0)
        self.Tree.column("ISBN", width=100)
        self.Tree.column("Titulo", width=140)
        self.Tree.column("Autor", width=120)
        self.Tree.column("Editorial", width=120)
        self.Tree.column("Categoria", width=80)
        self.Tree.column("Estado", width=60)
        self.Tree.column("Fecha_Ingreso", width=70)
        
        # Posicionar el Tree
        self.Tree.place(relx=0.06, rely=0.20)
        
        # Llenar datos
        conexion.cargar_datos(self.Tree)
        
        # CRUD
        self.BtnNuevo = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Nuevo, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.open_add_record_window)
        self.BtnNuevo.place(relx=0.13, rely=0.06)
        tooltip.Hovertip(self.BtnNuevo, text='Agregar nuevo registro', hover_delay=100)
        
        self.BtnEliminar = ctk.CTkButton(self.FrGrilla, width=60, height=50, image=self.Eliminar, text='', fg_color='#005066', border_width=1, border_color='#FFFFFF', command=self.eliminar_dato)
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
        libros = conexion.obtener_libros()
        self.CbItems = ctk.CTkComboBox(self.FrDatos, fg_color='#FFFFFF', text_color='#000000', font=('Roboto', 18),  width=320, button_color='#f09641', values=libros, state='readonly')
        self.CbItems.place(relx=0.29, rely=0.62)
        
        # Btn Guardar
        self.BtnGuardar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Guardar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Guardar, hover=True, hover_color='#002029', command=self.Guardar_Prestamo)
        self.BtnGuardar.place(relx=0.25, rely=0.72)
        
        # Btn Cancelar
        self.BtnCancelar = ctk.CTkButton(self.FrDatos, fg_color='#005066', text='Cancelar', font=('Roboto', 18, 'bold'), width=150, height=80, border_color='#FFFFFF', border_width=1, compound='left', image=self.Cancelar, hover=True, hover_color='#002029')
        self.BtnCancelar.place(relx=0.50, rely=0.72)

    # Commands
    def Home(self):
        self.Loans_Form()
    def open_add_record_window(self):
        # Crear una nueva ventana encima de la principal
        add_window = tk.Toplevel(self.FrInventory)
        add_window.title("Agregar Nuevo Registro")
        add_window.config(bg="#002029")
    
        # Obtener las dimensiones de la pantalla y la ventana principal
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()
        window_width = 400
        window_height = 400

        # Calcular la posición centrada en la pantalla
        position_top = int((screen_height / 2) - (window_height / 2))
        position_left = int((screen_width / 2) - (window_width / 2))

        # Establecer la geometría para centrar la ventana
        add_window.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        # Desactivar la opción de redimensionar
        add_window.resizable(False, False)
    
        # Etiquetas y campos de entrada para los datos
        label_codigo = tk.Label(add_window, text="Código", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_codigo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.TxtCodigoAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtCodigoAdd.grid(row=0, column=1, padx=10, pady=10)

        label_titulo = tk.Label(add_window, text="Titulo", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_titulo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.TxtTituloAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtTituloAdd.grid(row=1, column=1, padx=10, pady=10)

        label_autor = tk.Label(add_window, text="Autor", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_autor.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.TxtAutorAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtAutorAdd.grid(row=2, column=1, padx=10, pady=10)

        label_Editorial = tk.Label(add_window, text="Editorial", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_Editorial.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.TxtEditorialAdd = tk.Entry(add_window, font=("Roboto", 12))
        self.TxtEditorialAdd.grid(row=3, column=1, padx=10, pady=10)

        label_categoria = tk.Label(add_window, text="Categoría", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_categoria.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.CbItemsAdd = ttk.Combobox(add_window, values=["Distopía", "Clásico", "Misterio", "Romance"], font=("Roboto", 12))
        self.CbItemsAdd.grid(row=4, column=1, padx=10, pady=10)
    
        label_estado = tk.Label(add_window, text="Estado", font=("Roboto", 12), bg="#002029", fg="#FFFFFF")
        label_estado.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.CbEstadoAdd = ttk.Combobox(add_window, values=["Disponible", "No disponible"], font=("Roboto", 12))
        self.CbEstadoAdd.grid(row=5, column=1, padx=10, pady=10)

        # Botón para guardar el nuevo registro
        save_button = tk.Button(add_window, text="Guardar", font=("Roboto", 12), bg="#005066", fg="#FFFFFF", command=self.save_new_record)
        save_button.grid(row=6, column=0, columnspan=2, pady=20)
    
        # Botón para cerrar la ventana emergente
        cancel_button = tk.Button(add_window, text="Cancelar", font=("Roboto", 12), bg="#D32F2F", fg="#FFFFFF", command=add_window.destroy)
        cancel_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Hacer que la ventana se cierre automáticamente cuando se presione el botón "Guardar"
        add_window.transient(self.FrInventory)
        add_window.grab_set()
    def save_new_record(self):
        # Obtener los datos de los campos de entrada
        codigo = self.TxtCodigoAdd.get()
        titulo = self.TxtTituloAdd.get()
        autor = self.TxtAutorAdd.get()
        editorial = self.TxtEditorialAdd.get()
        categoria = self.CbItemsAdd.get()
        estado = self.CbEstadoAdd.get()
    
        # Verificar si todos los campos están llenos
        if not codigo or not titulo or not autor or not editorial or not categoria or not estado:
            print("Por favor complete todos los campos")
            return
    
        # Insertar los datos en la base de datos
        conexion.insertar_dato(codigo, titulo, autor, editorial, categoria, estado)
    
        # Cerrar la ventana de agregar registro
        self.TxtCodigoAdd.delete(0, tk.END)
        self.TxtTituloAdd.delete(0, tk.END)
        self.TxtAutorAdd.delete(0, tk.END)
        self.TxtEditorialAdd.delete(0, tk.END)
        self.CbItemsAdd.set('')
        self.CbEstadoAdd.set('')
    
        # Recargar los datos en el Treeview de la ventana principal
        self.Inventory_Panel()
    def eliminar_dato(self):
        # Obtener el ID del item seleccionado
        selected_item = self.Tree.selection()

        if not selected_item:  # Verificar si se ha seleccionado algún item
            mb.showwarning("Selección vacía", "Por favor, selecciona un registro para eliminar.")
            return

        # Obtener los valores del item seleccionado
        item_values = self.Tree.item(selected_item)['values']
    
        # Suponiendo que 'ISBN' es el primer valor del item, lo usamos para eliminar el registro
        isbn = item_values[0]

        # Confirmar con el usuario si desea eliminar el registro
        confirm = mb.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el registro con ISBN: {isbn}?")

        if confirm:
            # Llamar a la función para eliminar el registro de la base de datos
            try:
             # Suponiendo que la función `conexion.eliminar_dato(isbn)` elimina el registro de la base de datos
                conexion.eliminar_dato(isbn)
            
                # Eliminar el item del Treeview
                self.Tree.delete(selected_item)

                # Mostrar mensaje de éxito
                mb.showinfo("Eliminación exitosa", f"El registro con ISBN {isbn} ha sido eliminado.")
        
            except Exception as e:
                # Si ocurre algún error, mostrar un mensaje
                mb.showerror("Error", f"Hubo un error al intentar eliminar el registro: {e}")
        # Obtener los valores de los campos
    def consultar_dinamicamente(self, event):
        # Obtener el texto de la caja de texto de consulta
        search_text = self.TxtConsulta.get().lower()
    
        for item in self.Tree.get_children():
            self.Tree.delete(item)
    
        all_data = conexion.obtener_datos()
    
        filtered_data = []
        for record in all_data:
            if any(search_text in str(field).lower() for field in record):
                filtered_data.append(record)
    
        for record in filtered_data:
            self.Tree.insert("", "end", values=record)
        mb.showwarning(title="Resultado", message=mensaje).show()
        
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
        self.BtnSalir = ctk.CTkButton(self.FrNav, fg_color='#005066', text='Cerrar Sesion', image=self.Salir, width=250, height=10, compound='left', corner_radius=0, font=('Roboto', 18, 'bold'), anchor='w', border_spacing=10, hover=False)
        self.BtnSalir.place(relx=0, rely=0.92)
def Start():
    App()