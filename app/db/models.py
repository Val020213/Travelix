from sqlalchemy import Column, Integer, String, Float, Time, ForeignKey, Date
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

    excursions = relationship('ExcursionModel', secondary='agency_excursion_association', back_populates='agencies')
    offers = relationship('OfferModel', secondary='agency_offer', back_populates='agencies')
    extended_excursions = relationship('ExtendedExcursionModel', secondary='package', back_populates='agency')
    packages = relationship('PackageModel', back_populates='agency')
    package_reservations = relationship('PackageModel', secondary='package_reservation', back_populates='agency')
    facilities = relationship('FacilityModel', secondary='package_facility', back_populates='agency')

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

    agencies = relationship('AgencyModel', secondary='agency_excursion_association', back_populates='excursions')
    tourist_reservations = relationship('TouristModel', secondary='excursion_reservation', back_populates='excursions')

class ExtendedExcursionModel(Base):

    __tablename__ = 'extended_excursion'

    id = Column(Integer, primary_key=True, nullable=False)
    excursion_id = Column(Integer, ForeignKey('excursion.id'), nullable=False)

    excursion = relationship('ExcursionModel', back_populates='extended_excursion', uselist=False)
    agency = relationship('AgencyModel', secondary='package', back_populates='extended_excursions')
    packages = relationship('PackageModel', back_populates='extended_excursion')
    package_reservations = relationship('PackageModel', secondary='package_reservation', back_populates='extended_excursion')
    facilities = relationship('FacilityModel', secondary='package_facility', back_populates='extended_excursion')
    hotel = relationship('HotelModel', secondary='hotel_extended_excursion_association', back_populates='extended_excursions')


ExcursionModel.extended_excursion = relationship('ExtendedExcursionModel', back_populates='excursion', uselist=False)
class FacilityModel(Base):

    __tablename__ = 'facility'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String(100), nullable=False)

    packages = relationship('PackageModel', secondary='package_facility', back_populates='facilities')
    agencies = relationship('AgencyModel', secondary='package_facility', back_populates='facilities')
    extended_excursions = relationship('ExtendedExcursionModel', secondary='package_facility', back_populates='facilities')
class HotelModel(Base):
    
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    category = Column(Integer, nullable=False)

    offers = relationship('OfferModel', back_populates='hotel')
    extended_excursions = relationship('ExtendedExcursionModel', secondary='hotel_extended_excursion_association', back_populates='hotel')

class OfferModel(Base):

    __tablename__ = 'offer'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    price = Column(Float, nullable=False)
    description = Column(String(100), nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotel.id'))

    hotel = relationship('HotelModel', back_populates='offers')
    agencies = relationship('AgencyModel', secondary='agency_offer', back_populates='offers')

class PackageModel(Base):

    __tablename__ = 'package'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    duration = Column(Integer, nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    agency_id = Column(Integer, ForeignKey('agency.id'))
    extended_excursion_id = Column(Integer, ForeignKey('extended_excursion.id'))

    agency = relationship('AgencyModel', back_populates='packages')
    extended_excursion = relationship('ExtendedExcursionModel', back_populates='packages')
    tourist_reservations = relationship('TouristModel', secondary='package_reservation', back_populates='packages')
    facilities = relationship('FacilityModel', secondary='package_facility', back_populates='packages')

class TouristModel(Base):

    __tablename__ = 'tourist'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    nationality = Column(String(50), nullable=False)

    tourist_types = relationship('TouristTypeModel', secondary='tourist_type_tourist_association', back_populates='tourists')
    excursion_reservations = relationship('ExcursionModel', secondary='excursion_reservation', back_populates='tourists')
    package_reservations = relationship('PackageModel', secondary='package_reservation', back_populates='tourists')

class TouristTypeModel(Base):

    __tablename__ = 'tourist_type'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)

    tourists = relationship('TouristModel', secondary='tourist_type_tourist_association', back_populates='tourist_types')








#Associations
    
class AgencyExcursionAssociationModel(Base):

    __tablename__ = 'agency_excursion_association'

    agency_id = Column(Integer, ForeignKey('agency.id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('excursion.id'), primary_key=True)

    agency = relationship('AgencyModel', back_populates='excursions')
    excursion = relationship('ExcursionModel', back_populates='agencies')

class AgencyOfferModel(Base):

    __tablename__ = 'agency_offer'

    agency_id = Column(Integer, ForeignKey('agency.id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('offer.id'), primary_key=True)
    price = Column('price', Float, nullable=False)

    agency = relationship('AgencyModel', back_populates='offers')
    offer = relationship('OfferModel', back_populates='agencies')


class ExcursionReservationModel(Base):

    __tablename__ = 'excursion_reservation'

    tourist_id = Column(Integer, ForeignKey('tourist.id'), primary_key=True)
    excursion_id = Column(Integer, ForeignKey('excursion.id'), primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)

    tourist = relationship('TouristModel', back_populates='excursion_reservations')
    excursion = relationship('ExcursionModel', back_populates='tourist_reservations')

class PackageReservationModel(Base):

    __tablename__ = 'package_reservation'

    tourist_id = Column(Integer, ForeignKey('tourist.id'), primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'), primary_key=True)
    agency_id = Column(Integer, ForeignKey('agency.id'), primary_key=True)
    extended_excursion_id = Column(Integer, ForeignKey('extended_excursion.id'), primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)

    tourist = relationship('TouristModel', back_populates='package_reservations')
    package = relationship('PackageModel', back_populates='tourist_reservations')
    agency = relationship('AgencyModel', back_populates='package_reservations')
    extended_excursion = relationship('ExtendedExcursionModel', back_populates='package_reservations')

class PackageFacilityModel(Base):

    __tablename__ = 'package_facility'

    package_id = Column(Integer, ForeignKey('package.id'), primary_key=True)
    agency_id = Column(Integer, ForeignKey('agency.id'), primary_key=True)
    extended_excursion = Column(Integer, ForeignKey('extended_excursion.id'), primary_key=True)
    facility_id = Column(Integer, ForeignKey('facility.id'), primary_key=True)

    package = relationship('PackageModel', back_populates='facilities')
    facility = relationship('FacilityModel', back_populates='packages')
    agency = relationship('AgencyModel', back_populates='facilities')
    extended_excursion = relationship('ExtendedExcursionModel', back_populates='facilities')

class TouristTypeTouristAssociationModel(Base):

    __tablename__ = 'tourist_type_tourist_association'

    tourist_type_id = Column(Integer, ForeignKey('tourist_type.id'), primary_key=True)
    tourist_id = Column(Integer, ForeignKey('tourist.id'), primary_key=True)

    tourist_type = relationship('TouristTypeModel', back_populates='tourists')
    tourist = relationship('TouristModel', back_populates='tourist_types')

class HotelExtendedExcursionAssociation(Base):

    __tablename__ = 'hotel_extended_excursion_association'

    hotel_id = Column(Integer, ForeignKey('hotel.id'), primary_key=True)
    extended_excursion_id = Column(Integer, ForeignKey('extended_excursion.id'), primary_key=True)
    departure_date = Column(Date, nullable=False, primary_key=True)
    arrival_date = Column(Date, nullable=False, primary_key=True)

    hotel = relationship('HotelModel', back_populates='extended_excursions')
    extended_excursion = relationship('ExtendedExcursionModel', back_populates='hotel')