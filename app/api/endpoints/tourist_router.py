from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from db.config import get_db

from api.routes import routers
from schemas.schema import TouristSchema, TouristCreate, Token, TokenData
from db.models import TouristModel
import db.crud.auth_crud as crud


router = APIRouter(prefix="/tourist", tags=["tourist"])
routers.include_router(router)


@router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db)):
    return crud.login_for_access_token(db)


@router.post("/create")
async def create_user(tourist: TouristCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, tourist)


@router.get("/me", response_model=TouristSchema)
async def read_users_me(current_user: TouristModel = Depends(crud.get_current_active_user)):
    return current_user
