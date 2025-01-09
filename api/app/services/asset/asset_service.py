from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.asset import Asset
from app.schemas.asset import AssetCreate
from datetime import datetime

class AssetService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_asset(self, asset_data: AssetCreate, organization_id: int) -> Asset:
        asset = Asset(
            **asset_data.dict(),
            organization_id=organization_id,
            created_at=datetime.utcnow()
        )
        self.db.add(asset)
        await self.db.commit()
        await self.db.refresh(asset)
        return asset

    async def get_organization_assets(self, organization_id: int) -> list[Asset]:
        query = select(Asset).where(Asset.organization_id == organization_id)
        result = await self.db.execute(query)
        return result.scalars().all()
