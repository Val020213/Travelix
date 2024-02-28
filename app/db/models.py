from sqlalchemy import Column, Integer, String
from db.config import Base

class AgencyModel(Base):
    
    __tablename__ = 'agency'

    agency_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    agency_name = Column(String(50), nullable=False)
    agency_address = Column(String(100), nullable=False)
    fax_number = Column(Integer, nullable=False)
    email = Column(String(100), nullable=False)

class TouristModel(Base):

    __tablename__ = 'tourist'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False)
    nationallity = Column(String(50), nullable=False)