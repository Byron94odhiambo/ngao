# api/app/api/v1/endpoints/mobile_money.py
@router.get("/security/mpesa/{org_id}", response_model=Dict)
async def check_mpesa_security(
    org_id: int,
    subscription: SubscriptionManager = Depends()
):
    """Check M-PESA integration security"""
    if not await subscription.can_access_feature(org_id, 'mobile_money_checks'):
        raise HTTPException(status_code=403, detail="Feature not available in current subscription")
    
    checker = MPESASecurityChecker()
    results = await checker.check_integration_security(org_id)
    return results