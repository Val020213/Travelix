from fastapi import APIRouter, HTTPException, Path, Depends
from db.config import get_db
from sqlalchemy.orm import Session
from schemas.schema import UserSchema
import db.crud as crud


router = APIRouter(prefix="/user", tags=["user"])

@router.get('/list')
async def list_users(db:Session=Depends(get_db)):
    return crud.get_users(db,0,5)
    