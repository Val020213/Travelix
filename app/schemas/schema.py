from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    password : Optional[str]=None
    phone : Optional[str]
    email : Optional[str]


class AgencySchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    agency_address : Optional[str]=None
    fax_number : Optional[int]=None
    email : Optional[str]=None

class TouristSchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    nationallity : Optional[str]=None

class RoleSchema(BaseModel):
    name : Optional[str]=None