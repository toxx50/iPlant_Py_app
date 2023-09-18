import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class MyProfilePage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.myprofile_frame = tk.Frame(self, bg='#181818')
        self.myprofile_frame.pack_propagate(False)
        self.myprofile_frame.configure(width=1100, height=700)

        self.loginLabel = tk.Label(self, text="MY PROFILE", font=('arial', 22, 'bold'), bg='#181818', fg='white')
        self.loginLabel.place(x=20,y=100)

        self.loginLabel =  tk.Button(self, text="EDIT USER",font=('arial', 15, 'bold'), width=15,height=1, bd=0,
                               bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white')
        self.loginLabel.place(x=20, y=200)

        #REGION log-in image
        self.login_img = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/login_logo.png')
        self.login_img.resize((50,50))
        photo = ImageTk.PhotoImage(self.login_img)
        self.login_img_label = tk.Label(self, image=photo, bg='#181818')
        self.login_img_label.image = photo
        self.login_img_label.place(x=665, y=50)
        #NEDREGION

        #REGION username
        self.usrnam_label = tk.Label(self,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)
        #ENDREGION

        #REGION password
        self.passwrd_label = tk.Label(self,text='password', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.passwrd_label.place(x=585, y=350, width=150, height=20)

        self.psw_nameEntry = tk.Entry(self, highlightthickness=0,relief="flat", bg='#181818', fg='dark grey',
                                      font=('arial',13),show='*')
        self.psw_nameEntry.place(x=650, y=380, width=150, height=20)

        self.usr_name_line = tk.Canvas(self, width=260, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.usr_name_line.place(x=615, y=404)
        #ENDREGION


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




        self.myprofile_frame.pack()