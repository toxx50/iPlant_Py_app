from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PlantsInfo(Base):
    __tablename__ = 'plants'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String(20))
    photo = Column('Photo', String)
    soil_moisture = ('Soil moisture', String)


    #dodati sve o biljci šta treba sadržavati u bazi podataka
    #svjetlost, hlad...dali dodavat kakvu prehranu



"""
Bok,

Moraš napraviti u bazi podataka za biljke, tj u ovom folderu sljedece:

a) Kreirat profil biljke: 
    - id biljke
    - ime biljke
    - path do filea biljke
    - vlažnost tla
    - izloženost suncu ili hladu
    - toplije ili hladnije mjesto
    - dodavanje supstrata ili hrane
    - mjesto u kojoj posudi pripada
    - starost biljke (datum kad je posađena)
   
b) Mogućnost editiranja biljke:
    - uklanjanje biljke
    - premještanje biljke
    - dodavanje vode i hrane

c) dodavanje slika biljaka i bio(o biljkama) u folder s resursima.

d) dodavanje nove bilje u posudu

e) u kodu povlači podatke iz baze o biljci i 
    prikazuje sve u GUI (naziv, sliku, info)
    
f) dopunjavanje tj sync-anje novim podatcima o biljkama (temp, vlažnost itd.)




    






"""