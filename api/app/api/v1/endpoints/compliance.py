# api/app/api/v1/endpoints/compliance.py
@router.get("/compliance/dpa/{org_id}", response_model=Dict)
async def check_dpa_compliance(
    org_id: int,
    subscription: SubscriptionManager = Depends()
):
    """Check DPA compliance status"""
    if not await subscription.can_access_feature(org_id, 'basic_compliance'):
        raise HTTPException(status_code=403, detail="Feature not available in current subscription")
    
    checker = DPAComplianceChecker()
    results = await checker.check_compliance(org_id)
    return results