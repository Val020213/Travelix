from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field


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

class RoleSchema(BaseModel):
    name : Optional[str]=None