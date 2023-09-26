from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PlantsInfo(Base):
    __tablename__ = 'plants'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Name', String(20))
    soil_moisture = Column('Soil moisture', String)
    sun_exposure = Column('Sun exposure', String)
    temperature_exposure = Column('Temperature', String)
    food = Column('Food', String)
    planter = Column('Planter', Integer)
    photo = Column('Photo', String)

    def __init__(self, name, soil_mosture, sun_exposure, temperature_exposure, food, planter, photo):
        self.name = name
        self.soil_mosture = soil_mosture
        self.sun_exposure = sun_exposure
        self.temperature_exposure = temperature_exposure
        self.food = food
        self.planter = planter
        self.photo = photo

engine = create_engine('sqlite:///C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/db-direct/plants_data.db', echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


plants = session.query(PlantsInfo)




# DATABASE
# db_user = User(ssn, first, last, username, password, admin)
# session.add(db_user)
# session.commit()



""" Planter(vaza) ima svoj ID koji onda pripada u bazi podataka Biljke pod 'Planter(Int)' """
""" Onemogućiti dodavanje biljke ako ne postoji slobodnih mjesta u vazi, prvo se mora postavit nova vaza za novu biljku"""

"""
Bok,

Moraš napraviti u bazi podataka za biljke, tj u ovom folderu sljedece:

a) Kreirat profil biljke: 
    - id biljke x
    - ime biljke x 
    - path do filea biljke x
    - vlažnost tla x
    - izloženost suncu ili hladu x
    - toplije ili hladnije mjesto x
    - dodavanje supstrata ili hrane x
    - mjesto u kojoj posudi pripada x
   
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