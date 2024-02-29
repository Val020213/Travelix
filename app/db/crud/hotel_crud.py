from sqlalchemy.orm import Session
from db.models import  HotelModel
from schemas.schema import HotelSchema


def get_hotels(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(HotelModel).offset(skip).limit(limit).all())

def get_hotel_by_id(db:Session,hotel_id:int):
    return toSchema(db.query(HotelModel).filter(HotelModel.id==hotel_id).first())

def create_hotel(db:Session,hotel_schema:HotelSchema):
    hotel=toModel(hotel_schema)
    db.add(hotel)
    db.commit()
    db.refresh(hotel)
    return "Success"

def remove_hotel(db:Session,hotel_id:int):
    hotel=get_hotel_by_id(db,hotel_id)
    db.delete(hotel)
    db.commit()
    return "Success"

def update_hotel(db:Session,hotel_schema:HotelSchema):
    hotel=get_hotel_by_id(db,hotel_schema.id)
    hotel=toModel(hotel_schema)
    db.commit()
    db.refresh(hotel)
    return toSchema(hotel)

def toModel(hotel_schema:HotelSchema) -> HotelModel:
    return HotelModel(id=hotel_schema.id,name=hotel_schema.name,
                      address=hotel_schema.address,category=hotel_schema.category)

def toSchema(hotel_model:HotelModel) -> HotelSchema:
    return HotelSchema(id=hotel_model.id,name=hotel_model.name,
                       address=hotel_model.address,category=hotel_model.category)