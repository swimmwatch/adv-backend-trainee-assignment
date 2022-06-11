"""
Advert service routers
"""
from fastapi import APIRouter

from services.advert.routers import advert

api_router = APIRouter()
api_router.include_router(advert.router)
