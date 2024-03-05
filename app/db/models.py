from sqlalchemy import Column, Integer, String, Float, Time, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.config import Base


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(50), nullable=False)
    hashed_password = Column(String(50), nullable=False)
    phone = Column(String(10))
    email = Column(String(100))


class AgencyModel(Base):

    __tablename__ = "agency"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    fax_number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)

    excursions = relationship(
        "ExcursionModel",
        secondary="agency_excursion_association"
    )
    offers = relationship(
        "OfferModel", secondary="agency_offer"
    )
    extended_excursions = relationship(
        "ExtendedExcursionModel", secondary="package"
    )
    packages = relationship("PackageModel")
    package_reservations = relationship(
        "PackageModel", secondary="package_reservation"
    )
    facilities = relationship(
        "FacilityModel", secondary="package_facility"
    )


class ExcursionModel(Base):

    __tablename__ = "excursion"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    departure_place = Column(String(100), nullable=False)
    departure_day = Column(String(50), nullable=False)
    departure_hour = Column(Time, nullable=False)
    arrival_place = Column(String(100), nullable=False)
    arrival_day = Column(String(50), nullable=False)
    arrival_hour = Column(Time, nullable=False)
    price = Column(Float, nullable=False)

    # agencies = relationship(
    #     "AgencyModel",
    #     secondary="agency_excursion_association"
    # )
    # tourists = relationship(
    #     "TouristModel", secondary="excursion_reservation"
    # )


class ExtendedExcursionModel(Base):

    __tablename__ = "extended_excursion"

    id = Column(Integer, primary_key=True, nullable=False)
    excursion_id = Column(Integer, ForeignKey("excursion.id"), nullable=False)

    excursion = relationship(
        "ExcursionModel", uselist=False
    )
    agencies = relationship(
        "AgencyModel", secondary="package_reservation"
    )
    tourist = relationship("TouristModel", secondary="package_reservation")
    packages = relationship(
        "PackageModel",
        secondary="package_reservation"
    )
    facilities = relationship(
        "FacilityModel",
        secondary="package_facility"
    )
    hotel = relationship(
        "HotelModel",
        secondary="hotel_extended_excursion_association",
    )


ExcursionModel.extended_excursion = relationship(
    "ExtendedExcursionModel", uselist=False
)


class FacilityModel(Base):

    __tablename__ = "facility"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    description = Column(String(100), nullable=False)

    packages = relationship(
        "PackageModel", secondary="package_facility"
    )
    agencies = relationship(
        "AgencyModel", secondary="package_facility"
    )
    extended_excursions = relationship(
        "ExtendedExcursionModel",
        secondary="package_facility"
    )


class HotelModel(Base):

    __tablename__ = "hotel"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    category = Column(Integer, nullable=False)

    offers = relationship("OfferModel")
    extended_excursions = relationship("ExtendedExcursionModel",
                                       secondary="hotel_extended_excursion_association")


class OfferModel(Base):

    __tablename__ = "offer"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    price = Column(Float, nullable=False)
    description = Column(String(100), nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotel.id"))

    hotel = relationship("HotelModel", uselist=False)
    agencies = relationship(
        "AgencyModel", secondary="agency_offer"
    )


class PackageModel(Base):

    __tablename__ = "package"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    duration = Column(Integer, nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    agency_id = Column(Integer, ForeignKey("agency.id"))
    extended_excursion_id = Column(Integer, ForeignKey("extended_excursion.id"))

    # agency = relationship("AgencyModel", back_populates="agency")
    # extended_excursions = relationship(
    #     "ExtendedExcursionModel"
    # )
    tourist_reservations = relationship(
        "TouristModel", secondary="package_reservation"
    )
    facilities = relationship(
        "FacilityModel", secondary="package_facility"
    )


class TouristModel(Base):

    __tablename__ = "tourist"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    nationality = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(50), nullable=False)

    tourist_types = relationship(
        "TouristTypeModel",
        secondary="tourist_type_tourist_association"
    )
    excursion = relationship(
        "ExcursionModel", secondary="excursion_reservation"
    )
    package = relationship(
        "PackageModel", secondary="package_reservation"
    )


class TouristTypeModel(Base):

    __tablename__ = "tourist_type"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)

    tourists = relationship(
        "TouristModel",
        secondary="tourist_type_tourist_association"
    )


# Associations


class AgencyExcursionAssociationModel(Base):

    __tablename__ = "agency_excursion_association"

    agency_id = Column(Integer, ForeignKey("agency.id"), primary_key=True)
    excursion_id = Column(Integer, ForeignKey("excursion.id"), primary_key=True)

    # agencies = relationship("AgencyModel", back_populates="agency")
    # excursion = relationship("ExcursionModel", back_populates="excursion")


class AgencyOfferModel(Base):

    __tablename__ = "agency_offer"

    agency_id = Column(Integer, ForeignKey("agency.id"), primary_key=True)
    excursion_id = Column(Integer, ForeignKey("offer.id"), primary_key=True)
    price = Column("price", Float, nullable=False)

    # agencies = relationship("AgencyModel", back_populates="agency")
    # offers = relationship("OfferModel", back_populates="offer")


class ExcursionReservationModel(Base):

    __tablename__ = "excursion_reservation"

    tourist_id = Column(Integer, ForeignKey("tourist.id"), primary_key=True)
    excursion_id = Column(Integer, ForeignKey("excursion.id"), primary_key=True)
    date = Column(Date, nullable=False, primary_key=True)

    # tourists = relationship("TouristModel", back_populates="tourist")
    # excursion = relationship("ExcursionModel", back_populates="excursion")


class PackageReservationModel(Base):

    __tablename__ = "package_reservation"

    tourist_id = Column(Integer, ForeignKey("tourist.id"), primary_key=True)
    package_id = Column(Integer, ForeignKey("package.id"), primary_key=True)
    agency_id = Column(Integer, ForeignKey("agency.id"), primary_key=True)
    extended_excursion_id = Column(
        Integer, ForeignKey("extended_excursion.id"), primary_key=True
    )
    date = Column(Date, nullable=False, primary_key=True)

    # tourist = relationship("TouristModel", back_populates="tourist")
    # packages = relationship("PackageModel", back_populates="package")
    # agency = relationship("AgencyModel", back_populates="agency")
    # extended_excursion = relationship(
    #     "ExtendedExcursionModel", back_populates="extended_excursion"
    # )


class PackageFacilityModel(Base):

    __tablename__ = "package_facility"

    package_id = Column(Integer, ForeignKey("package.id"), primary_key=True)
    agency_id = Column(Integer, ForeignKey("agency.id"), primary_key=True)
    extended_excursion = Column(Integer, ForeignKey("extended_excursion.id"), primary_key=True)
    facility_id = Column(Integer, ForeignKey("facility.id"), primary_key=True)

    # packages = relationship("PackageModel", back_populates="package")
    # facilities = relationship("FacilityModel", back_populates="facility")
    # agencies = relationship("AgencyModel", back_populates="agency")
    # extended_excursions = relationship("ExtendedExcursionModel", back_populates="extended_excursion")
class TouristTypeTouristAssociationModel(Base):

    __tablename__ = "tourist_type_tourist_association"

    tourist_type_id = Column(Integer, ForeignKey("tourist_type.id"), primary_key=True)
    tourist_id = Column(Integer, ForeignKey("tourist.id"), primary_key=True)

    # tourist_type = relationship("TouristTypeModel", back_populates="tourist_type")
    # tourist = relationship("TouristModel", back_populates="tourist")


class HotelExtendedExcursionAssociation(Base):

    __tablename__ = "hotel_extended_excursion_association"

    hotel_id = Column(Integer, ForeignKey("hotel.id"), primary_key=True)
    extended_excursion_id = Column(
        Integer, ForeignKey("extended_excursion.id"), primary_key=True
    )
    departure_date = Column(Date, nullable=False, primary_key=True)
    arrival_date = Column(Date, nullable=False, primary_key=True)

    # hotel = relationship("HotelModel", back_populates="hotel")
    # extended_excursions = relationship("ExtendedExcursionModel", back_populates="extended_excursion")
