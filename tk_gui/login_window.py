from tk_gui.front_page import *
from constants.all_constants import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image



class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.title("iPlants PY")
        img = tk.PhotoImage(file=MAIN_ICON)
        self.geometry("1200x800")
        self.resizable(0,0)
        self.iconphoto(False, img)

        self.login_window = LogInWindow(self)


class LogInWindow(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0,y=0,relheight=1,relwidth=1)



        # Background image
        self.bg_frame = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/leaves-plant-dark-green-shade-4k_1540574301.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self,image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')


        # Login frame
        self.lgn_frame = tk.Frame(self, bg='#181818',width='900',height='600')
        self.lgn_frame.place(x=150,y=100)

        self.signInLabel = tk.Label(self.lgn_frame, text="Sign in", font=('arial',22,'bold'), bg='#181818',fg='white')
        self.signInLabel.place(x=585,y=190, width=300,height=30)

        # Username
        self.usrnam_label = tk.Label(self.lgn_frame,text='username', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.usrnam_label.place(x=580, y=270, width=150, height=20)

        self.usr_nameEntry = tk.Entry(self.lgn_frame,highlightthickness=0,relief="flat", bg='#181818', fg='dark gray',
                                      font=('arial',13))
        self.usr_nameEntry.place(x=650,y=300, width=150,height=20)

        self.usr_name_line = tk.Canvas(self.lgn_frame, width=260, height=2.0, bg='#bdb9b1',highlightthickness=0)
        self.usr_name_line.place(x=615,y=324)

        # Username icon
        self.side_img_usr = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/usr_icon.png')
        photo = ImageTk.PhotoImage(self.side_img_usr)
        self.side_img_usr_label = tk.Label(self.lgn_frame, image=photo, bg='#181818')
        self.side_img_usr_label.image = photo
        self.side_img_usr_label.place(x=615, y=295)

        # Password
        self.passwrd_label = tk.Label(self.lgn_frame,text='password', font=('arial',15),bg='#181818',fg='#4f4e4d')
        self.passwrd_label.place(x=585, y=350, width=150, height=20)

        self.psw_nameEntry = tk.Entry(self.lgn_frame, highlightthickness=0,relief="flat", bg='#181818', fg='dark grey',
                                      font=('arial',13),show='*')
        self.psw_nameEntry.place(x=650, y=380, width=150, height=20)

        self.usr_name_line = tk.Canvas(self.lgn_frame, width=260, height=2.0, bg='#bdb9b1', highlightthickness=0)
        self.usr_name_line.place(x=615, y=404)

        # Password icon
        self.side_img_key = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/key_icon.png')
        photo = ImageTk.PhotoImage(self.side_img_key)
        self.side_img_key_label = tk.Label(self.lgn_frame, image=photo, bg='#181818')
        self.side_img_key_label.image = photo
        self.side_img_key_label.place(x=615, y=375)

        # left side image
        self.side_img = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/IoT-1222.png')
        photo = ImageTk.PhotoImage(self.side_img)
        self.side_img_label = tk.Label(self.lgn_frame,image=photo,bg='#181818')
        self.side_img_label.image = photo
        self.side_img_label.place(x=5,y=100)


        # log-in image
        self.login_img = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/login_logo.png')
        photo = ImageTk.PhotoImage(self.login_img)
        self.login_img_label = tk.Label(self.lgn_frame, image=photo, bg='#181818')
        self.login_img_label.image = photo
        self.login_img_label.place(x=665, y=50)


        # login button
        self.login_button = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/login_button.png')
        photo = ImageTk.PhotoImage(self.login_button)
        self.login_button_label = tk.Label(self.lgn_frame, image=photo, bg='#181818')
        self.login_button_label.image = photo
        self.login_button_label.place(x=615, y=430)

        self.login = tk.Button(self.login_button_label, text='LOGIN', font=('arial',15,'bold'), width=19, bd=0, bg='#138b61', cursor='hand2', activebackground='#138b61', fg='white', command=self.delete_login_page)
        self.login.place(x=10,y=5)

        # show/hide password button
        self.show_image = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/hide_pass1.png')
        self.photo1 = ImageTk.PhotoImage(self.show_image)
        self.show_button = tk.Button(self.lgn_frame, image=self.photo1, bg='#181818', activebackground='#4f4e4d', cursor='hand2',bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=850,y=355)

        self.hide_image = Image.open('C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/show_pass.png')
        self.photo2 = ImageTk.PhotoImage(self.hide_image)

    def show(self):
        self.hide_button = tk.Button(self.lgn_frame, image=self.photo2, bg='#181818', activebackground='#4f4e4d', cursor='hand2',bd=0,command=self.hide)
        self.hide_button.image = self.photo2
        self.hide_button.place(x=850,y=355)
        self.psw_nameEntry.config(show='')

    def hide(self):
        self.show_button = tk.Button(self.lgn_frame, image=self.photo1, bg='#181818', activebackground='#4f4e4d',
                                     cursor='hand2', bd=0, command=self.show)
        self.show_button.image = self.photo1
        self.show_button.place(x=850, y=355)
        self.psw_nameEntry.config(show='*')

    def delete_login_page(self):
        #for frame in self.lgn_frame.winfo_children():
        self.lgn_frame.destroy()
        self.home = FrontPage()








#trenutno postavljeno da mogu pokretat kod
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()








