import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from sql_files.sqlalchemy_users_db import *


MAIN_ICON='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/plant_628280.png'

HOME_TEMP_PIC='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/template-pothos_menu.png'

POT_PICTURE='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/pot_6388536.png'
POT_PICTURE_BLACK='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/pot_6388542.png'

PLANT_PICTURE='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/sprout_2713484.png'
PLANT_PICTURE_BLACK='C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/gui_files/sprout_2713467.png'

DESCRIPTION = 'Plant: Name'

'Plant: Name\nContainer: Name\nAge: weeks\nSoil: wet/dry'



for user in users:
    if user.firstname == 'Ivan':
        print('There is Ivan here')
    elif user.firstname == 'Tomislav':
        print('Hello Tomislav here')

"""
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.username = username
        self.password = password
        self.email = email
"""

def user_first_name():
    for user in users:
        return user.firstname

def user_last_name():
    for user in users:
        return user.lastname

def user_username():
    for user in users:
        return user.username

def user_password():
    for user in users:
        return user.password

def user_password_hide():
    x = ''
    for char in user_password():
        x += '*'
    return x

def user_city():
    for user in users:
        return user.city

def user_email():
    for user in users:
        return user.email

