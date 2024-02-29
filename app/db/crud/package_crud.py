from sqlalchemy.orm import Session
from db.models import  PackageModel
from schemas.schema import PackageSchema


def get_packages(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(PackageModel).offset(skip).limit(limit).all())

def get_package_by_id(db:Session,package_id:int):
    return toSchema(db.query(PackageModel).filter(PackageModel.id==package_id).first())

def create_package(db:Session,package_schema:PackageSchema):
    package=toModel(package_schema)
    db.add(package)
    db.commit()
    db.refresh(package)
    return "Success"

def remove_package(db:Session,package_id:int):
    package=get_package_by_id(db,package_id)
    db.delete(package)
    db.commit()
    return "Success"

def update_package(db:Session,package_schema:PackageSchema):
    package=get_package_by_id(db,package_schema.id)
    package=toModel(package_schema)
    db.commit()
    db.refresh(package)
    return toSchema(package)

def toModel(package_schema:PackageSchema) -> PackageModel:
    return PackageModel(id=package_schema.id,duration=package_schema.duration,
                        description=package_schema.description,price=package_schema.price)

def toSchema(package_model:PackageModel) -> PackageSchema:
    return PackageSchema(id=package_model.id,duration=package_model.duration,
                         description=package_model.description,price=package_model.price)