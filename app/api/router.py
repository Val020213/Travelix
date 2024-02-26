from fastapi import APIRouter, HTTPException, Path, Depends
from db.config import get_db
from sqlalchemy.orm import Session
from schemas.schema import AgencySchema
import db.crud as crud

router = APIRouter(prefix="/agency", tags=["agency"])

@router.get('/list')
async def list_agencies(db:Session=Depends(get_db)):
    _agency = crud.get_agencies(db,0,5)
    return _agency