from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from db.config import get_db

from schemas.schema import AgencySchema
import db.crud as crud


router = APIRouter(prefix="/agency", tags=["agency"])


@router.get("/list")
async def list_agencies(db: Session = Depends(get_db)):
    _agency = crud.get_agencies(db, 0, 5)
    return _agency


@router.get("/{agency_id}")
async def get_agency_by_id(
    agency_id: int = Path(..., title="The ID of the agency"),
    db: Session = Depends(get_db),
):
    _agency = crud.get_agency_by_id(db, agency_id)
    if _agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    return _agency


@router.post("/create")
async def create_agency(agency: AgencySchema, db: Session = Depends(get_db)):
    return crud.create_agency(db, agency)


@router.delete("/remove/{agency_id}")
async def remove_agency(
    agency_id: int = Path(..., title="The ID of the agency"),
    db: Session = Depends(get_db),
):
    return crud.remove_agency(db, agency_id)


@router.put("/update")
async def update_agency(agency: AgencySchema, db: Session = Depends(get_db)):
    return crud.update_agency(db, agency)
