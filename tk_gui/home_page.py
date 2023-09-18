from constants.all_constants import *
#from constants.pictures_file import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class HomePage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.home_frame = tk.Frame(self, bg='#181818')
        self.home_frame.pack_propagate(False)
        self.home_frame.configure(width=1100, height=700)



        #scrollbar frame
        self.right_frame = tk.LabelFrame(self.home_frame, bg='grey')
        self.right_frame.place(x=500,y=50, width=550, height=600)

        self.my_canvas = tk.Canvas(self.right_frame)
        self.my_canvas.pack(side='left', fill='both', expand='yes')

        self.my_scrollbar = ttk.Scrollbar(self.right_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox('all')))

        self.second_frame = tk.Frame(self.my_canvas)

        self.my_canvas.create_window((0,0), window=self.second_frame, anchor='nw')

        """
        self.second_frame.columnconfigure(0, weight=1)
        self.second_frame.columnconfigure(1, weight=1)
        self.second_frame.columnconfigure(2, weight=1)
        self.second_frame.columnconfigure(3, weight=1)

        self.second_frame.grid(sticky='n')"""

        self.hom_temp_img = Image.open(HOME_TEMP_PIC).resize((150, 150))
        HOME_TEMP_IMG = ImageTk.PhotoImage(self.hom_temp_img)
        self.label_middle= tk.Label(self, image=HOME_TEMP_IMG)
        self.label_middle.image = HOME_TEMP_IMG
        self.label_middle.place(x=100,y=200)
        #self.sync_btn = tk.Button(self, text="SYNC",font=('arial', 10, 'bold'), width=10, bd=0,
        #                       bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white')
        #self.sync_btn.place(x=800,y=10)

        #self.loginLabel = tk.Label(self, text="Sign in", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        #self.loginLabel.place(x=100,y=100)

        #self.loginLabel = tk.Label(self, text="Sign in", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        #self.loginLabel.place(x=100, y=200)

        for i in range(21):
            #this is for plant image
            self.loginLabel2 = tk.Label(self.second_frame, image=HOME_TEMP_IMG,bg='grey'
                                        ).grid(row=i, column=0,pady=5,padx=5)

            #this is for plant description
            self.loginLabel2 = tk.Label(self.second_frame, text=DESCRIPTION,
                                        font=('arial', 22),
                                        fg='dark grey').grid(row=i, column=1,pady=10,padx=50, sticky='n')



        self.home_frame.pack()
