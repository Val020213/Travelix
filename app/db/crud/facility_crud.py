from sqlalchemy.orm import Session
from db.models import  FacilityModel
from schemas.schema import FacilitySchema


def get_facilities(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(FacilityModel).offset(skip).limit(limit).all())

def get_facility_by_id(db:Session,id:int):
    return toSchema(db.query(FacilityModel).filter(FacilityModel.id==id).first())

def create_facility(db:Session,facility:FacilitySchema):
    db_facility = FacilityModel(name=facility.name)
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return toSchema(db_facility)

def update_facility(db:Session,id:int,facility:FacilitySchema):
    db_facility = db.query(FacilityModel).filter(FacilityModel.id==id).first()
    db_facility.name = facility.name
    db.commit()
    db.refresh(db_facility)
    return toSchema(db_facility)

def remove_facility(db:Session,id:int):
    db_facility = db.query(FacilityModel).filter(FacilityModel.id==id).first()
    db.delete(db_facility)
    db.commit()
    return "Success"

def toSchema(facility:FacilityModel) -> FacilitySchema:
    return FacilitySchema(id=facility.id,name=facility.name)

def toModel(facility:FacilitySchema) -> FacilityModel:
    return FacilityModel(name=facility.name)