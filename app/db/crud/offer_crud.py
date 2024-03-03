from sqlalchemy.orm import Session
from db.models import  OfferModel
from schemas.schema import OfferSchema


def get_offers(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(OfferModel).offset(skip).limit(limit).all())

def get_offer_by_id(db:Session,offer_id:int):
    return toSchema(db.query(OfferModel).filter(OfferModel.id==offer_id).first())

def create_offer(db:Session,offer_schema:OfferSchema):
    offer=toModel(offer_schema)
    db.add(offer)
    db.commit()
    db.refresh(offer)
    return "Success"

def remove_offer(db:Session,offer_id:int):
    offer=get_offer_by_id(db,offer_id)
    db.delete(offer)
    db.commit()
    return "Success"

def update_offer(db:Session,offer_schema:OfferSchema):
    offer=get_offer_by_id(db,offer_schema.id)
    offer=toModel(offer_schema)
    db.commit()
    db.refresh(offer)
    return toSchema(offer)

def toModel(offer_schema:OfferSchema) -> OfferModel:
    return OfferModel(id=offer_schema.id,price=offer_schema.price,
                        description=offer_schema.description)

def toSchema(offer_model:OfferModel) -> OfferSchema:
    return OfferSchema(id=offer_model.id,price=offer_model.price,
                         description=offer_model.description)