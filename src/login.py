import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk

class App():
    def __init__(self):
        
        # Ventana principal
        self.FrmLogin = tk.Tk()
        self.FrmLogin.overrideredirect(True)
        self.FrmLogin.config(background='#002029')

        # Variables
        sprite = Image.open('img/logo/Logo_FT.png')
        sprite = ImageTk.PhotoImage(sprite)
        
        # Creacion de Elementos
        self.LblLogo = ctk.CTkLabel(self.FrmLogin, image=sprite, text='')
        self.FrLogin = ctk.CTkFrame(self.FrmLogin, width=300, height=300, fg_color='#004052', corner_radius=20)
        self.TxtUser = ctk.CTkEntry(self.FrLogin, corner_radius=20, placeholder_text='USUARIO', placeholder_text_color='#FFFFFF', fg_color='#005066', border_width=0, width=230)
        self.TxtPass = ctk.CTkEntry(self.FrLogin, corner_radius=20, placeholder_text='CONTRASEÑA', placeholder_text_color='#FFFFFF', fg_color='#005066', border_width=0, width=230)
        self.BtnLogin = ctk.CTkButton(self.FrLogin, corner_radius=20, fg_color='#00607A', text_color='#FFFFFF', text='Ingresar', hover=True, hover_color='#002029')
        
        # Posicionamiento de Elementos
        self.LblLogo.place(relx=0.01, rely=0.001)
        self.FrLogin.place(relx=0.60, rely=0.25)
        self.TxtUser.place(relx=0.12, rely=0.30)
        self.TxtPass.place(relx=0.12, rely=0.50)
        self.BtnLogin.place(relx=0.27, rely=0.70)
        
        # Funciones
        self.centerWindow()
        self.FrmLogin.mainloop()
    
    def centerWindow(self):
        
        W, H = 850, 500
        
        Ws = (self.FrmLogin.winfo_screenwidth()//2) - (W//2)
        Hs = (self.FrmLogin.winfo_screenheight()//2) - (H//2)
        
        self.FrmLogin.geometry(f'{W}x{H}+{Ws}+{Hs}')
def Start():
    App()