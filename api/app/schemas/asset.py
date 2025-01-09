from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AssetBase(BaseModel):
    name: str
    type: str
    ip_address: Optional[str] = None
    hostname: Optional[str] = None

class AssetCreate(AssetBase):
    pass

class AssetResponse(AssetBase):
    id: int
    organization_id: int
    created_at: datetime

    class Config:
        from_attributes = True
