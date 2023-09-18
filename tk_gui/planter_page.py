from constants.all_constants import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


"""FILE ZA TEGLE"""

class PlanterPage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.planter_frame = tk.Frame(self, bg='#181818')
        self.planter_frame.pack_propagate(False)
        self.planter_frame.configure(width=1100, height=700)

        self.sync_btn = tk.Button(self, text="SYNC",font=('arial', 10, 'bold'), width=10, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white')
        self.sync_btn.place(x=950,y=15)

        # scrollbar frame
        self.right_frame = tk.LabelFrame(self.planter_frame, bg='grey')
        self.right_frame.place(x=500, y=50, width=550, height=600)

        self.my_canvas = tk.Canvas(self.right_frame)
        self.my_canvas.pack(side='left', fill='both', expand='yes')

        self.my_scrollbar = ttk.Scrollbar(self.right_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox('all')))

        self.second_frame = tk.Frame(self.my_canvas)

        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor='nw')

        self.pot_img = Image.open(POT_PICTURE).resize((150, 150))
        POT_IMG = ImageTk.PhotoImage(self.pot_img)
        self.pot_img.image = POT_IMG

        self.pot_img_bl = Image.open(POT_PICTURE_BLACK).resize((150, 150))
        POT_IMG_BL = ImageTk.PhotoImage(self.pot_img_bl)
        self.pot_img_bl.image = POT_IMG_BL

        """        
        self.loginLabel = tk.Label(self, text="WAZUUP", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=20,y=600)

        self.loginLabel = tk.Label(self, text="Sign in", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=580, y=600)

        """
        for i in range(21):
            #this is for plant image
            self.loginLabel2 = tk.Label(self.second_frame, image=POT_IMG,bg='grey'
                                        ).grid(row=i, column=0,pady=5,padx=5)

            #this is for plant description
            self.loginLabel2 = tk.Label(self.second_frame, text=DESCRIPTION,
                                        font=('arial', 22,),
                                        fg='dark grey').grid(row=i, column=1,pady=10,padx=50)

        self.add_planter_lbl = tk.Label(self.second_frame, image=POT_IMG_BL, bg='grey'
                                    ).grid(row=i+1, column=0, pady=5, padx=5)
        self.add_planter_btn = tk.Button(self.second_frame,text='+\n\nADD PLANTER' ,font=('arial', 20, 'bold'), width=15, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white').grid(row=i+1,column=1, ipady=10,ipadx=10,pady=10,padx=50)






        self.planter_frame.pack()