from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PlanterInfo(Base):
    __tablename__ = 'planter'

    id = Column('ID', Integer, primary_key=True)
    name = Column('Planter name', String)
    soil_moisture = Column('Soil moisture', String)
    soil_temperature = Column('Soil temperature', String)
    soil_food = Column('Food', String)
    capacity = Column('Plant capacity', Integer)
    capacity_status = Column('Status', Integer)

    def __init__(self, name: str, soil_moisture: str, soil_temperature: str, soil_food: str, capacity: int, capacity_status:int):
        self.name = name
        self.soil_moisture = soil_moisture
        self.soil_temperature = soil_temperature
        self.soil_food = soil_food
        self.capacity = capacity
        self.capacity_status = capacity_status


engine = create_engine('sqlite:///C:/Users/Korisnik/PycharmProjects/DATA SCIENCE/PyFlora_app/db-direct/planter_data.db', echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

planter = session.query(PlanterInfo)


#db_planter = PlanterInfo('Vaza 1', 'vlažno', '10', 'none', 2,0)
#session.add(db_planter)
#session.commit()



"""
Planter:

a) mora imati svoj ID
b) kapacitet biljaka
c) prazan, djelomično popunjen, pun
d) vlažna/suha zemlja, sa hranom ili bez
e) ...?

"""