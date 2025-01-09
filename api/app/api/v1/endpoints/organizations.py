from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.deps import get_db
from app.schemas.auth import OrganizationRegistration
from app.services.onboarding.onboarding_service import OnboardingService
from typing import Dict

router = APIRouter()

@router.post("/register", response_model=Dict)
async def register_organization(
    org_data: OrganizationRegistration,
    db: AsyncSession = Depends(get_db)
):
    """Register new organization"""
    try:
        onboarding = OnboardingService(db)
        result = await onboarding.register_organization(
            org_data.organization.dict(),
            org_data.admin.dict()
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Registration error: {str(e)}")  # For debugging
        raise HTTPException(status_code=500, detail="Internal server error")
