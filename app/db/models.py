from sqlalchemy import Column, Integer, String
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
