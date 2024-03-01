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
    offers : List["OfferAgencyAssociation"] = []
    extended_excursions : List["ExtendedExcursion"] = []
    packages : List["Package"] = []
class AgencyOfferAssociation(BaseModel):
    agency_id : Optional[int]=None
    offer_id : Optional[int]=None
    price : Optional[float]=None    


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



class ExtendedExcursionSchema(BaseModel):
    excursion_id : Optional[int]=None
class ExtendedExcursionCreate(ExtendedExcursionSchema):
    pass
class ExtendedExcursion(ExtendedExcursionSchema):
    id: int
    excursion: ExcursionSchema
    agency: List["Agency"] = []
    packages: List["Package"] = []

class TouristSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    nationality : Optional[str]=None


class TouristTypeSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None


class HotelSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    address : Optional[str]=None
    category : Optional[int]=None

class OfferSchema(BaseModel):
    price : Optional[float]=None
    description : Optional[str]=None
class OfferCreate(OfferSchema):
    pass
class Offer(OfferSchema):
    id : Optional[int]=None
    hotel: HotelSchema
    agencies: List["AgencyOfferAssociation"] = []
class OfferAgencyAssociation(BaseModel):
    offer_id : Optional[int]=None
    agency_id : Optional[int]=None
    price : Optional[float]=None

class FacilitySchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None

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
