from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

class AgencySchema(BaseModel):
    id : Optional[int]=None
    name : Optional[str]=None
    agency_address : Optional[str]=None
    fax_number : Optional[int]=None
    email : Optional[str]=None