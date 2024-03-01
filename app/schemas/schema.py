from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from datetime import time
from typing import List


class UserSchema(BaseModel):
    id : Optional[int]=None
    username : Optional[str]=None
    password : Optional[str]=None
    phone : Optional[str]=None
    email : Optional[str]=None


class AgencySchema(BaseModel):
    name : Optional[str]=None
    address : Optional[str]=None
    fax_number : Optional[int]=None
    email : Optional[str]=None
class AgencyCreate(AgencySchema):
    pass
class Agency(AgencySchema):
    id : Optional[int]=None
    excursions : List["Excursion"] = []
    offers : List["AgencyOfferAssociation"] = []
    extended_excursions : List["ExtendedExcursion"] = []
    packages : List["Package"] = []
    package_reservations : List["PackageReservationAssociation"] = []
    facilities : List["PackageFacilityAssociation"] = []

  


class ExcursionSchema(BaseModel):
    departure_place : Optional[str]=None
    departure_day : Optional[str]=None
    departure_hour : Optional[time]=None
    arrival_place : Optional[str]=None
    arrival_day : Optional[str]=None
    arrival_hour : Optional[time]=None
    price : Optional[float]=None
class ExcursionCreate(ExcursionSchema):
    pass
class Excursion(ExcursionSchema):
    id : Optional[int]=None
    agencies: List["Agency"] = []
    tourists: List["ExcursionReservationAssociation"] = []


class ExtendedExcursionSchema(BaseModel):
    excursion_id : Optional[int]=None
class ExtendedExcursionCreate(ExtendedExcursionSchema):
    pass
class ExtendedExcursion(ExtendedExcursionSchema):
    id: int
    excursion: ExcursionSchema
    agency: List["Agency"] = []
    packages: List["Package"] = []
    package_reservations: List["PackageReservationAssociation"] = []
    facilities: List["PackageFacilityAssociation"] = []
    hotel: List["HotelExtendedExcursionAssociation"] = []


class TouristSchema(BaseModel):
    name : Optional[str]=None
    nationality : Optional[str]=None

class TouristCreate(TouristSchema):
    pass
class Tourist(TouristSchema):
    id : Optional[int]=None
    tourist_type: List["TouristType"] = []
    excursions: List["ExcursionReservationAssociation"] = []
    packages: List["PackageReservationAssociation"] = []


class TouristTypeSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None

class TouristTypeCreate(TouristTypeSchema):
    pass
class TouristType(TouristTypeSchema):
    id : Optional[int]=None
    tourists: List["Tourist"] = []


class HotelSchema(BaseModel):
    name : Optional[str]=None
    address : Optional[str]=None
    category : Optional[int]=None
class HotelCreate(HotelSchema):
    pass
class Hotel(HotelSchema):
    id : Optional[int]=None
    extended_excursions: List["HotelExtendedExcursionAssociation"] = []

class OfferSchema(BaseModel):
    price : Optional[float]=None
    description : Optional[str]=None
class OfferCreate(OfferSchema):
    pass
class Offer(OfferSchema):
    id : Optional[int]=None
    hotel: HotelSchema
    agencies: List["AgencyOfferAssociation"] = []

class FacilitySchema(BaseModel):
    name : Optional[str]=None
class FacilityCreate(FacilitySchema):
    pass
class Facility(FacilitySchema):
    id : Optional[int]=None
    packages: List["PackageFacilityAssociation"] = []

class PackageSchema(BaseModel):
    duration : Optional[int]=None
    description : Optional[str]=None
    price : Optional[float]=None

class PackageCreate(PackageSchema):
    pass
class Package(PackageSchema):
    id : Optional[int]=None
    agency: List["Agency"] = []
    extended_excursion: List["ExtendedExcursion"] = []
    package_reservations: List["PackageReservationAssociation"] = []
    facilities: List["PackageFacilityAssociation"] = []






#Associations
class ExcursionReservationAssociation(BaseModel):
    tourist_id : Optional[int]=None
    excursion_id : Optional[int]=None
    date : Optional[str]=None
    tourist: Optional[Tourist]=None
    excursion: Optional[Excursion]=None

class PackageReservationAssociation(BaseModel):
    tourist_id : Optional[int]=None
    package_id : Optional[int]=None
    agency_id : Optional[int]=None
    extended_excursion_id : Optional[int]=None
    date : Optional[str]=None
    tourist: Optional[Tourist]=None
    package: Optional[Package]=None
    agency: Optional[Agency]=None
    extended_excursion: Optional[ExtendedExcursion]=None

class AgencyOfferAssociation(BaseModel):
    agency_id : Optional[int]=None
    offer_id : Optional[int]=None
    price : Optional[float]=None  
    agency: Optional[Agency]=None
    offer: Optional[Offer]=None

class PackageFacilityAssociation(BaseModel):
    package_id : Optional[int]=None
    agency_id : Optional[int]=None
    extended_excursion_id : Optional[int]=None
    facility_id : Optional[int]=None
    package: Optional[Package]=None
    agency: Optional[Agency]=None
    extended_excursion: Optional[ExtendedExcursion]=None
    facility: Optional[Facility]=None

class HotelExtendedExcursionAssociation(BaseModel):
    hotel_id : Optional[int]=None
    extended_excursion_id : Optional[int]=None
    hotel: Optional[Hotel]=None
    extended_excursion: Optional[ExtendedExcursion]=None