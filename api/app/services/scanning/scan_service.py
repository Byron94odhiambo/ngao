from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.scan_result import ScanResult
from app.models.asset import Asset
from typing import Dict, Optional

class ScanService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def run_vulnerability_scan(self, asset_id: int) -> Dict:
        """Run a vulnerability scan on an asset"""
        # Get the asset
        asset = await self._get_asset(asset_id)
        if not asset:
            raise ValueError(f"Asset with ID {asset_id} not found")

        # Create scan record
        scan_result = ScanResult(
            asset_id=asset_id,
            scan_type="vulnerability",
            status="in_progress",
            created_at=datetime.utcnow()
        )
        self.db.add(scan_result)
        await self.db.flush()

        try:
            # Simulate scanning process
            findings = await self._simulate_scan(asset)
            
            # Update scan result
            scan_result.status = "completed"
            scan_result.findings = findings
            scan_result.completed_at = datetime.utcnow()
            await self.db.commit()

            return {
                "scan_id": scan_result.id,
                "status": "completed",
                "findings": findings,
                "completed_at": scan_result.completed_at
            }

        except Exception as e:
            scan_result.status = "failed"
            scan_result.findings = {"error": str(e)}
            await self.db.commit()
            raise

    async def _get_asset(self, asset_id: int) -> Optional[Asset]:
        """Get asset by ID"""
        return await self.db.get(Asset, asset_id)

    async def _simulate_scan(self, asset: Asset) -> Dict:
        """Simulate a vulnerability scan"""
        return {
            "vulnerabilities": [
                {
                    "severity": "high",
                    "title": "Outdated Software Version",
                    "description": "The server is running an outdated version with known vulnerabilities",
                    "recommendation": "Update to the latest secure version"
                },
                {
                    "severity": "medium",
                    "title": "Insecure Configuration",
                    "description": "Default configuration settings detected",
                    "recommendation": "Apply security hardening guidelines"
                }
            ],
            "security_score": 75,
            "scan_time": datetime.utcnow().isoformat(),
            "asset_details": {
                "name": asset.name,
                "type": asset.type,
                "ip_address": asset.ip_address,
                "hostname": asset.hostname
            }
        }
