# api/app/api/v1/endpoints/scans.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict
from app.services.scanners.network_scanner import NetworkScanner
from app.services.subscription.subscription_manager import SubscriptionManager

router = APIRouter()

@router.post("/scan/network/", response_model=Dict)
async def run_network_scan(
    org_id: int,
    target: str,
    subscription: SubscriptionManager = Depends()
):
    """Run network security scan"""
    if not await subscription.can_access_feature(org_id, 'network_scan'):
        raise HTTPException(status_code=403, detail="Feature not available in current subscription")
    
    scanner = NetworkScanner()
    results = await scanner.scan_network(target)
    return results