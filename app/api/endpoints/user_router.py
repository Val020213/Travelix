from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from db.config import get_db

from api.routes import routers
from schemas.schema import UserSchema
from db.crud import user_crud as crud


router = APIRouter(prefix="/user", tags=["user"])
routers.include_router(router)

@router.get('/list')
async def list_users(db:Session=Depends(get_db)):
    return crud.get_users(db,0,5)
    