import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from constants.all_constants import *


class MyProfilePage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.myprofile_frame = tk.Frame(self, bg='#181818')
        self.myprofile_frame.pack_propagate(False)
        self.myprofile_frame.configure(width=1100, height=700)

        self.loginLabel = tk.Label(self, text='MY PROFILE', font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=50,y=50)

        self.loginLabel =  tk.Button(self, text="EDIT USER",font=('arial', 15, 'bold'), width=15,height=1, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white')
        self.loginLabel.place(x=50, y=100)

        #REGION profile info FRAME 1
        self.myprofile_frame_info1 = tk.Frame(self.myprofile_frame, bg='#0e3352')
        self.myprofile_frame_info1.place(x=400,y=50,width=650, height=300)
        #ENDREGION

        #REGION profile info FRAME 2
        self.myprofile_frame_info2 = tk.Frame(self.myprofile_frame, bg='light grey')
        self.myprofile_frame_info2.place(x=400,y=350,width=650, height=300)
        #ENDREGION


        #REGION log-in image
        self.user_img = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/user_logo.png')
        self.user_img.resize((50,50))
        photo = ImageTk.PhotoImage(self.user_img)
        self.user_img_label = tk.Label(self.myprofile_frame_info1, image=photo, bg='#0e3352')
        self.user_img_label.image = photo
        self.user_img_label.place(x=50, y=25)
        #ENDREGION

        #REGION username
        self.usrnam_label = tk.Label(self.myprofile_frame_info1,text=f'{user_first_name()} {user_last_name()}', font=('arial',20),bg='#0e3352',fg='grey')
        self.usrnam_label.place(x=250, y=60)


        #ENDREGION

        #REGION email
        self.email_label = tk.Label(self.myprofile_frame_info1,text=f'{user_email()}', font=('arial',12),bg='#0e3352',fg='grey')
        self.email_label.place(x=250, y=100)

        self.usr_name_line = tk.Canvas(self.myprofile_frame_info1, width=600, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=25,y=175)
        #ENDREGION

        #REGION password
        self.city_label = tk.Label(self.myprofile_frame_info2,text=f'City', font=('arial',17),bg='light grey',fg='grey')
        self.city_label.place(x=50, y=30)

        self.city_db_label = tk.Label(self.myprofile_frame_info2,text=f'{user_city()}', font=('arial',17),bg='light grey',fg='grey')
        self.city_db_label.place(x=600, y=30, anchor='ne')

        self.username_label = tk.Label(self.myprofile_frame_info2,text=f'Username', font=('arial',17),bg='light grey',fg='grey')
        self.username_label.place(x=50, y=80)

        self.username_db_label = tk.Label(self.myprofile_frame_info2,text=f'{user_username()}', font=('arial',17),bg='light grey',fg='grey')
        self.username_db_label.place(x=600, y=80, anchor='ne')

        self.password_label = tk.Label(self.myprofile_frame_info2,text=f'Password', font=('arial',17),bg='light grey',fg='grey')
        self.password_label.place(x=50, y=130)

        self.password_db_label = tk.Label(self.myprofile_frame_info2,text=f'{user_password_hide()}', font=('arial',17),bg='light grey',fg='grey')
        self.password_db_label.place(x=600, y=130, anchor='ne')



        """ DODATI BROJ PLANTSA SA DESNE I TAKOĐER DODATI BROJ PLANTERA """
        self.plants_label = tk.Label(self.myprofile_frame_info2,text=f'Number of plants', font=('arial',17),bg='light grey',fg='grey')
        self.plants_label.place(x=50, y=180)

        self.planter_label = tk.Label(self.myprofile_frame_info2,text=f'Number of planters', font=('arial',17),bg='light grey',fg='grey')
        self.planter_label.place(x=50, y=230)


        #ENDREGION


        """       
        #REGION first name
        self.usrnam_label = tk.Label(self,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)
        #ENDREGION

        #REGION last name
        self.usrnam_label = tk.Label(self,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)
        #ENDREGION

        #REGION  email
        self.usrnam_label = tk.Label(self,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)
        #ENDREGION

        #REGION city
        self.usrnam_label = tk.Label(self,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)
        #ENDREGION
        """




        self.myprofile_frame.pack()