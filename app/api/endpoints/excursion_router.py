from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from db.config import get_db

from schemas.schema import ExcursionSchema
import db.crud.excursion_crud as crud


router = APIRouter(prefix="/excursion", tags=["excursion"])


@router.get("/list")
async def get_excursions(db: Session = Depends(get_db)):
    _excursion = crud.get_excursions(db, 0, 5)
    return _excursion
