from fastapi import APIRouter
from app.api.v1.endpoints import auth, organizations, assets, scanning

api_router = APIRouter()

# Add routes without additional prefix since endpoints handle it
api_router.include_router(auth.router)
api_router.include_router(organizations.router)
api_router.include_router(assets.router)
api_router.include_router(scanning.router)
