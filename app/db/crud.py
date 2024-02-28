from sqlalchemy.orm import Session
from db.models import AgencyModel
from schemas.schema import AgencySchema
from db.models import UserModel

def get_agencies(db:Session,skip:int=0,limit:int=100):
    return db.query(AgencyModel).offset(skip).limit(limit).all()

def get_users(db:Session,skip:int=0,limit:int=100):
    return db.query(UserModel).offset(skip).limit(limit).all()