from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.models.asset import Asset
from app.schemas.asset import AssetCreate, AssetResponse
from typing import List
from datetime import datetime

router = APIRouter()

@router.post("", response_model=AssetResponse)
async def create_asset(
    asset_data: AssetCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create a new asset"""
    try:
        print(f"Creating asset for organization: {current_user.organization_id}")
        new_asset = Asset(
            name=asset_data.name,
            type=asset_data.type,
            ip_address=asset_data.ip_address,
            hostname=asset_data.hostname,
            organization_id=current_user.organization_id,
            created_at=datetime.utcnow()
        )
        db.add(new_asset)
        await db.commit()
        await db.refresh(new_asset)
        return new_asset
    except Exception as e:
        print(f"Error creating asset: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("", response_model=List[AssetResponse])
async def list_assets(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all assets for the organization"""
    try:
        query = select(Asset).where(Asset.organization_id == current_user.organization_id)
        result = await db.execute(query)
        assets = result.scalars().all()
        return [asset for asset in assets]
    except Exception as e:
        print(f"Error listing assets: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
