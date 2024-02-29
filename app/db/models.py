from sqlalchemy import Column, Integer, String, Float, Time, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.config import Base


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String(50), nullable=False)
    phone = Column(String(10))
    email = Column(String(100)) 

class AgencyModel(Base):
    
    __tablename__ = 'agency'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    fax_number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)

class TouristModel(Base):

    __tablename__ = 'tourist'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    nationality = Column(String(50), nullable=False)

class PackageModel(Base):

    __tablename__ = 'package'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    duration = Column(Integer, nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)

class ExcursionModel(Base):

    __tablename__ = 'excursion'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    departure_place = Column(String(100), nullable=False)
    departure_day = Column(String(50), nullable=False)
    departure_hour = Column(Time, nullable=False)
    arrival_place = Column(String(100), nullable=False)
    arrival_day = Column(String(50), nullable=False)
    arrival_hour = Column(Time, nullable=False)
    price = Column(Float, nullable=False)

class ExtendedExcursionModel(Base):

    __tablename__ = 'extended_excursion'

    id = Column(Integer, primary_key=True, nullable=False)
    excursion_id = Column(Integer, ForeignKey('excursion.id'))

    excursion = relationship('ExcursionModel', back_populates='extended_excursion', uselist=False)

ExcursionModel.extended_excursion = relationship('ExtendedExcursionModel', back_populates='excursion', uselist=False)
class OfferModel(Base):

    __tablename__ = 'offer'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    price = Column(Float, nullable=False)
    description = Column(String(100), nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotel.id'))

    hotel = relationship('HotelModel', back_populates='offers')

class HotelModel(Base):
    
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    category = Column(Integer, nullable=False)

    offers = relationship('OfferModel', back_populates='hotel')

class TouristTypeModel(Base):

    __tablename__ = 'tourist_type'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)

class FacilityModel(Base):

    __tablename__ = 'facility'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String(100), nullable=False)