from sqlalchemy.orm import Session
from db.models import  TouristModel
from schemas.schema import TouristSchema


def get_tourists(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(TouristModel).offset(skip).limit(limit).all())

def get_tourist_by_id(db:Session,tourist_id:int):
    return toSchema(db.query(TouristModel).filter(TouristModel.id==tourist_id).first())

def create_tourist(db:Session,tourist_schema:TouristSchema):
    tourist=toModel(tourist_schema)
    db.add(tourist)
    db.commit()
    db.refresh(tourist)
    return "Success"

def remove_tourist(db:Session,tourist_id:int):
    tourist=get_tourist_by_id(db,tourist_id)
    db.delete(tourist)
    db.commit()
    return "Success"

def update_tourist(db:Session,tourist_schema:TouristSchema):
    tourist=get_tourist_by_id(db,tourist_schema.id)
    tourist=toModel(tourist_schema)
    db.commit()
    db.refresh(tourist)
    return toSchema(tourist)

def toModel(tourist_schema:TouristSchema) -> TouristModel:
    return TouristModel(id=tourist_schema.id,name=tourist_schema.name,nationallity=tourist_schema.nationallity)

def toSchema(tourist_model:TouristModel) -> TouristSchema:
    return TouristSchema(id=tourist_model.id,name=tourist_model.name,nationallity=tourist_model.nationallity)