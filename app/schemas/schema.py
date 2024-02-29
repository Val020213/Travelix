from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from datetime import time


class UserSchema(BaseModel):
    id : Optional[int]=None
    username : Optional[str]=None
    password : Optional[str]=None
    phone : Optional[str]=None
    email : Optional[str]=None

class AgencySchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    address : Optional[str]=None
    fax_number : Optional[int]=None
    email : Optional[str]=None

class TouristSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    nationality : Optional[str]=None
class PackageSchema(BaseModel):
    id : Optional[int]=None
    duration : Optional[int]=None
    description : Optional[str]=None
    price : Optional[float]=None

class ExcursionSchema(BaseModel):
    id : Optional[int]=None
    departure_place : Optional[str]=None
    departure_day : Optional[str]=None
    departure_hour : Optional[time]=None
    arrival_place : Optional[str]=None
    arrival_day : Optional[str]=None
    arrival_hour : Optional[time]=None
    price : Optional[float]=None

class OfferSchema(BaseModel):
    id : Optional[int]=None
    price : Optional[float]=None
    description : Optional[str]=None

class HotelSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    address : Optional[str]=None
    category : Optional[int]=None

class TouristTypeSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None

class FacilitySchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None