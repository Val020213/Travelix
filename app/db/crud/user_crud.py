from sqlalchemy.orm import Session
from db.models import UserModel
from schemas.schema import UserSchema


def get_users(db:Session,skip:int=0,limit:int=100):
    return toSchema(db.query(UserModel).offset(skip).limit(limit).all())

def toModel(user_schema:UserSchema) -> UserModel:
    return UserModel(username=user_schema.username,password=user_schema.password)

def toSchema(user_model:UserModel) -> UserSchema:
    return UserSchema(username=user_model.username,password=user_model.password)