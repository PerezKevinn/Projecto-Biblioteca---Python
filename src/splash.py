import tkinter as tk
import customtkinter as ctk
import login
from tkinter import ttk
from PIL import Image, ImageTk

class App():
    def __init__(self):
        
        # Ventana principal
        self.FrmSplash = tk.Tk()
        self.FrmSplash.config(background='#002029')
        self.FrmSplash.overrideredirect(True)
        
        # Variables
        sprite = Image.open('img/logo/Logo_FT.png').resize([600,400])
        sprite = ImageTk.PhotoImage(sprite)
        
        # Creacion de Elementos
        self.LblLogo = ttk.Label(self.FrmSplash, image=sprite, background='#002029')
        self.PbLoad = ctk.CTkProgressBar(self.FrmSplash, corner_radius=13, progress_color='#FFFFFF',width=400 , mode='determinate', determinate_speed=0.5, indeterminate_speed=0.5)
        
        # Configuracion de Elementos
        self.PbLoad.set(0)
        
        # Posicionamiento de Elementos 
        self.LblLogo.place(relx=0.12, rely=0.001)
        self.PbLoad.place(relx=0.25, rely=0.90)

        # Funciones
        self.centerWindow()
        self.loading()
        self.FrmSplash.mainloop()
    
    def centerWindow(self):
         
         W = 800
         H = 400
         
         Ws = (self.FrmSplash.winfo_screenwidth()//2) - (W//2)
         Hs = (self.FrmSplash.winfo_screenheight()//2) - (H//2)
         
         self.FrmSplash.geometry(f'{W}x{H}+{Ws}+{Hs}')
    
    def loading(self):
        
        for i in range(101):
            self.PbLoad.start()
            self.PbLoad['value'] = i
            self.FrmSplash.update()
            self.FrmSplash.after(27)
            
        if i == 100:
            self.FrmSplash.destroy()
            login.Start()
App()