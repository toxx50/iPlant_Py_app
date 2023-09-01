import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


"""FILE ZA BILJKEEEE"""

class PlantPage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.plant_frame = tk.Frame(self, bg='#181818')
        self.plant_frame.pack_propagate(False)
        self.plant_frame.configure(width=1100, height=700)

        self.sync_btn = tk.Button(self, text="SYNC",font=('arial', 10, 'bold'), width=10, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white')
        self.sync_btn.place(x=800,y=600)

        self.loginLabel = tk.Label(self, text="Sign in", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=20,y=100)

        self.loginLabel = tk.Label(self, text="Sign in", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=80, y=100)

        self.plant_frame.pack()