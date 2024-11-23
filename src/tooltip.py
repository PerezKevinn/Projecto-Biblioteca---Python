import tkinter as tk
from idlelib.tooltip import Hovertip

class CustomHovertip(Hovertip):
        
    def showcontents(self):
        label = tk.Label(
            self.tipwindow, text=f' "{self.text}" ', justify=tk.LEFT,
            bg="#005066", fg="#005066", borderwidth=1,
            font=("Times New Roman", 12)
            )
        label.pack()
    