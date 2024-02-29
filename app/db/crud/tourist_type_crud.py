from sqlalchemy.orm import Session
from db.models import TouristTypeModel 
from schemas.schema import TouristTypeSchema


def get_tourist_types(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(TouristTypeModel).offset(skip).limit(limit).all())

def get_tourist_type_by_id(db:Session,tourist_type_id:int):
    return toSchema(db.query(TouristTypeModel).filter(TouristTypeModel.id==tourist_type_id).first())

def create_tourist_type(db:Session,tourist_type_schema:TouristTypeSchema):
    tourist_type=toModel(tourist_type_schema)
    db.add(tourist_type)
    db.commit()
    db.refresh(tourist_type)
    return "Success"

def remove_tourist_type(db:Session,tourist_type_id:int):
    tourist_type=get_tourist_type_by_id(db,tourist_type_id)
    db.delete(tourist_type)
    db.commit()
    return "Success"

def update_tourist_type(db:Session,tourist_type_schema:TouristTypeSchema):
    tourist_type=get_tourist_type_by_id(db,tourist_type_schema.id)
    tourist_type=toModel(tourist_type_schema)
    db.commit()
    db.refresh(tourist_type)
    return toSchema(tourist_type)

def toModel(tourist_type_schema:TouristTypeSchema) -> TouristTypeModel:
    return TouristTypeModel(id=tourist_type_schema.id,name=tourist_type_schema.name)

def toSchema(tourist_type_model:TouristTypeModel) -> TouristTypeSchema:
    return TouristTypeSchema(id=tourist_type_model.id,name=tourist_type_model.name)