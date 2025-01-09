from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.deps import get_db, get_current_user
from app.services.scanning.scan_service import ScanService
from app.models.user import User
from app.models.asset import Asset
from typing import Dict

router = APIRouter()

@router.post("/{asset_id}/scan")
async def start_scan(
    asset_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
) -> Dict:
    """Start a vulnerability scan for an asset"""
    try:
        # Verify asset belongs to user's organization
        query = select(Asset).where(
            Asset.id == asset_id,
            Asset.organization_id == current_user.organization_id
        )
        result = await db.execute(query)
        asset = result.scalar_one_or_none()

        if not asset:
            raise HTTPException(
                status_code=404,
                detail=f"Asset with ID {asset_id} not found or not authorized"
            )

        scan_service = ScanService(db)
        scan_result = await scan_service.run_vulnerability_scan(asset_id)
        return scan_result

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
