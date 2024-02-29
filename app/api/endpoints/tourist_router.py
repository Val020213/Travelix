from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from db.config import get_db

from api.routes import routers
from schemas.schema import TouristSchema
import db.crud.tourist_crud as crud


router = APIRouter(prefix="/tourist", tags=["tourist"])
routers.include_router(router)

@router.get('/list')
async def get_tourists(db:Session=Depends(get_db)):
    _tourist=crud.get_tourists(db)
    return _tourist

@router.get('/{id}')
async def get_tourist_by_id(id:int,db:Session=Depends(get_db)):
    _tourist=crud.get_tourist_by_id(db,id)
    if _tourist is None:
        raise HTTPException(status_code=404,detail="Tourist not found")
    return _tourist

@router.post('/create')
async def create_tourists(request:TouristSchema,db:Session=Depends(get_db)):
    return crud.create_tourist(db,request)
    
@router.post('/update')
async def update_tourist(request:TouristSchema,db:Session=Depends(get_db)):
    return crud.update_tourist(db,request)
    

