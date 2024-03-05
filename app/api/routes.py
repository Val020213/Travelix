from fastapi import APIRouter
from api.endpoints.excursion_router import router as excursion_router
from api.endpoints.tourist_router import router as tourist_router
from api.endpoints.agency_router import router as agency_router

routers = APIRouter()

routers.include_router(excursion_router)
routers.include_router(tourist_router)
routers.include_router(agency_router)
