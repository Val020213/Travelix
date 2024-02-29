from sqlalchemy.orm import Session
from db.models import AgencyModel
from schemas.schema import AgencySchema


def get_agency(db:Session,skip:int=0,limit:int=100):
    return db.query(AgencyModel).offset(skip).limit(limit).all()

def get_agency_by_id(db:Session,agency_id:int):
    return toSchema(db.query(AgencyModel).filter(AgencyModel.agency_id == agency_id).first())

def create_agency(db:Session,agency_schema:AgencySchema):
    agency = toModel(agency_schema)
    db.add(agency)
    db.commit()
    db.refresh(agency)
    return "Success"

def remove_agency(db:Session,agency_id:int):
    agency = get_agency_by_id(db,agency_id)
    db.delete(agency)
    db.commit()
    return "Success"

def update_agency(db:Session,agency_schema:AgencySchema):
    agency = get_agency_by_id(db,agency_schema.id)
    agency = toModel(agency_schema)
    db.commit()
    db.refresh(agency)
    return toSchema(agency)


def toModel(agency_schema:AgencySchema) -> AgencyModel:
    return AgencyModel()

def toSchema(agency_model:AgencyModel) -> AgencySchema:
    return AgencySchema()