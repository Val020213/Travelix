from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from db.models import TouristModel, Token, TokenData
from schemas.schema import TouristSchema, TouristCreate

SECRET_KEY = "d3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oath_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_tourist(db: Session, username: str):
    return db.query(TouristModel).filter(TouristModel.username == username).first()


def authenticate_tourist(db: Session, username: str, password: str):
    tourist = get_tourist(db, username)
    if not tourist:
        return False
    if not verify_password(password, tourist.password):
        return False
    return tourist


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


async def get_current_user(db: Session, token: str = Depends(oath_2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_tourist(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: TouristModel = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def login_for_access_token(
    db: Session, form_data: OAuth2PasswordRequestForm = Depends()
):
    tourist = authenticate_tourist(db, form_data.username, form_data.password)
    if not tourist:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": tourist.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def create_user(db: Session, tourist: TouristSchema):
    tourist = get_tourist(db, username=tourist.username)
    if tourist is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    tourist = ToModelTourist(tourist)
    db.add(tourist)
    db.commit()
    db.refresh(tourist)
    return "Success"


def ToSchemaTourist(tourist_model: TouristModel) -> TouristSchema:
    return TouristSchema(
        id=tourist_model.id,
        name=tourist_model.name,
        nationality=tourist_model.nationality,
        username=tourist_model.username,
    )


def ToModelTourist(tourist_schema: TouristSchema) -> TouristModel:
    return TouristModel(
        id=tourist_schema.id,
        name=tourist_schema,
        nationality=tourist_schema.nationality,
        username=tourist_schema.username,
    )


def ToModelTouristCreate(tourist_schema: TouristCreate) -> TouristModel:
    return TouristModel(
        id=tourist_schema.id,
        name=tourist_schema.name,
        nationality=tourist_schema.nationality,
        password=get_password_hash(tourist_schema.password),
        username=tourist_schema.username,
    )
