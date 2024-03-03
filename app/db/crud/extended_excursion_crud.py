from sqlalchemy.orm import Session
from app.db.models import ExtendedExcursionModel
from schemas.schema import ExtendedExcursionSchema


def get_extended_excursions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ExtendedExcursionModel).offset(skip).limit(limit).all()


def get_extended_excursion_by_id(db: Session, extended_excursion_id: int):
    return db.query(ExtendedExcursionModel).filter(ExtendedExcursionModel.id == extended_excursion_id).first()


def create_extended_excursion(db: Session, extended_excursion_schema: ExtendedExcursionSchema):
    extended_excursion = ExtendedExcursionModel(
        id=extended_excursion_schema.id,
        excursion_id=extended_excursion_schema.excursion_id
    )
    db.add(extended_excursion)
    db.commit()
    db.refresh(extended_excursion)
    return extended_excursion


def remove_extended_excursion(db: Session, extended_excursion_id: int):
    extended_excursion = get_extended_excursion_by_id(db, extended_excursion_id)
    db.delete(extended_excursion)
    db.commit()
    return "Success"


def update_extended_excursion(db: Session, extended_excursion_schema: ExtendedExcursionSchema):
    extended_excursion = get_extended_excursion_by_id(db, extended_excursion_schema.id)
    extended_excursion.excursion_id = extended_excursion_schema.excursion_id
    db.commit()
    db.refresh(extended_excursion)
    return extended_excursion


def toModel(extended_excursion_schema: ExtendedExcursionSchema) -> ExtendedExcursionModel:
    return ExtendedExcursionModel(
        id=extended_excursion_schema.id,
        excursion_id=extended_excursion_schema.excursion_id
    )


def toSchema(extended_excursion_model: ExtendedExcursionModel) -> ExtendedExcursionSchema:
    return ExtendedExcursionSchema(
        id=extended_excursion_model.id,
        excursion_id=extended_excursion_model.excursion_id
   )
