from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
     pass


class PlaceModel(Base):
    __tablename__ = 'places'
    id = Column(Integer, primary_key=True)
    place_name = Column('place_name', String)
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)
