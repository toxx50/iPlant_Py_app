from tk_gui.home_page import HomePage
from tk_gui.plant_page import PlantPage
from tk_gui.my_profile_page import MyProfilePage
from tk_gui.planter_page import PlanterPage
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class FrontPage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0, y=0, relheight=1, relwidth=1)

        self.home_bg_frame = tk.Frame(self, bg='#138b61', width='1200', height='800')
        self.home_bg_frame.place(x=0, y=0)

        self.taskbar_frame = tk.Frame(self, bg='dark grey', width='1100', height='50')
        self.taskbar_frame.place(x=50, y=25)

        self.main_frame = tk.Frame(self, bg='#181818')
        self.main_frame.place(x=50, y=75) #napravi frame kao i na IOT Home app
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=1100, height=700)

        self.taskbar_buttons = TaskBar(self.taskbar_frame, background='dark grey')
        self.taskbar_buttons.place(x=5,y=2)

        self.home_page = HomePage(self.main_frame)
        self.home_page.place(x=0,y=0)


        #funkcije za pozivanje frameova preko taskbara
    def home_pagee(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        self.home_page = HomePage(self.main_frame)
        self.home_page.place(x=0,y=0)

    def plant_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        self.plant_pag1 = PlantPage(self.main_frame)
        self.plant_pag1.place(x=0,y=0)

    def planter_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        self.planter_page_frame = PlanterPage(self.main_frame)
        self.planter_page_frame.place(x=0,y=0)

    def my_profile_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
        self.myprofile_page_frame = MyProfilePage(self.main_frame)
        self.myprofile_page_frame.place(x=0,y=0)



class TaskBar(tk.Frame):
    def __init__(self,master, background='light green'):
        super().__init__(master,background=background)
        self.grid_columnconfigure(0, weight=1)

        def home():
            obj = FrontPage()
            obj.home_pagee()

        def plant():
            obj = FrontPage()
            obj.plant_page()

        def planter():
            obj = FrontPage()
            obj.planter_page()

        def profile():
            obj = FrontPage()
            obj.my_profile_page()





        self.home_bt = tk.Button(self, text='HOME', font=('arial', 15, 'bold'), width=15, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white',
                                 command=home) #pozovi funkciju iz klase FrontPage
        self.home_bt.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

        self.planter_bt = tk.Button(self, text='PLANTER', font=('arial', 15, 'bold'), width=15, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white',
                                    command=planter)
        self.planter_bt.grid(row=0, column=1, padx=5, pady=5, sticky='ew')


        self.plants_bt = tk.Button(self, text='PLANTS', font=('arial', 15, 'bold'), width=15, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white',
                                   command=plant) #pozovi funkciju iz klase FrontPage
        self.plants_bt.grid(row=0, column=2, padx=5, pady=5, sticky='ew')


        self.myprofile_bt = tk.Button(self, text='MY PROFILE', font=('arial', 15, 'bold'), width=15, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white',
                                      command=profile)
        self.myprofile_bt.grid(row=0, column=3, padx=5, pady=5, sticky='ew')







from tk_gui.login_window import *
#trenutno postavljeno da mogu pokretat kod
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()

