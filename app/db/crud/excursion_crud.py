from sqlalchemy.orm import Session
from db.models import ExcursionModel
from schemas.schema import ExcursionSchema


def get_excursions(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(ExcursionModel).offset(skip).limit(limit).all())

def get_excursion_by_id(db:Session,excursion_id:int):
    return toSchema(db.query(ExcursionModel).filter(ExcursionModel.id==excursion_id).first())

def create_excursion(db:Session,excursion_schema:ExcursionSchema):
    excursion=toModel(excursion_schema)
    db.add(excursion)
    db.commit()
    db.refresh(excursion)
    return "Success"

def remove_excursion(db:Session,excursion_id:int):
    excursion=get_excursion_by_id(db,excursion_id)
    db.delete(excursion)
    db.commit()
    return "Success"

def update_excursion(db:Session,excursion_schema:ExcursionSchema):
    excursion=get_excursion_by_id(db,excursion_schema.id)
    excursion=toModel(excursion_schema)
    db.commit()
    db.refresh(excursion)
    return toSchema(excursion)

def toModel(excursion_schema:ExcursionSchema) -> ExcursionModel:
    return ExcursionModel(id=excursion_schema.id,departure_place=excursion_schema.departure_place,
                        departure_day=excursion_schema.departure_day,departure_hour=excursion_schema.departure_hour,
                        arrival_place=excursion_schema.arrival_place,arrival_day=excursion_schema.arrival_day,
                        arrival_hour=excursion_schema.arrival_hour,price=excursion_schema.price)

def toSchema(excursion_model:ExcursionModel) -> ExcursionSchema:
    return ExcursionSchema(id=excursion_model.id,departure_place=excursion_model.departure_place,
                         departure_day=excursion_model.departure_day,departure_hour=excursion_model.departure_hour,
                         arrival_place=excursion_model.arrival_place,arrival_day=excursion_model.arrival_day,
                         arrival_hour=excursion_model.arrival_hour,price=excursion_model.price)