from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'users'

    id = Column('ID',Integer, primary_key=True)
    firstname = Column('First', String(20))
    lastname = Column('Last', String)
    city = Column('City', String)
    username = Column('Username', String)
    password = Column('Password', String)
    email = Column('Email', String)

    def __init__(self, firstname, lastname, city, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.username = username
        self.password = password
        self.email = email


engine = create_engine('sqlite:///C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/db-direct/users_data.db', echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



users = session.query(UserInfo)