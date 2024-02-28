from sqlalchemy.orm import Session
from db.models import  TouristModel
from schemas.schema import TouristSchema


def get_tourists(db:Session,skip:int=0,limit:int=100):
    return db.query(TouristModel).offset(skip).limit(limit).all()

def get_tourist_by_id(db:Session,tourist_id:int):
    return db.query(TouristModel).filter(TouristModel.id==tourist_id).first()

def create_tourist(db:Session,tourist_schema:TouristSchema):
    _tourist=TouristModel(id=tourist_schema.id,name=tourist_schema.name,nationallity=tourist_schema.nationallity)
    db.add(_tourist)
    db.commit()
    db.refresh(_tourist)
    return _tourist

def remove_tourist(db:Session,tourist_id:int):
    _tourist=get_tourist_by_id(db,tourist_id)
    db.delete(_tourist)
    db.commit()

def update_tourist(db:Session,tourist_schema:TouristSchema):
    _tourist=get_tourist_by_id(db,tourist_schema.id)
    _tourist.name=tourist_schema.name
    _tourist.nationallity=tourist_schema.nationallity
    db.commit()
    db.refresh(_tourist)
    return _tourist