# api/app/api/v1/endpoints/reports.py
@router.get("/reports/{org_id}/{scan_id}", response_model=Dict)
async def get_security_report(
    org_id: int,
    scan_id: int,
    subscription: SubscriptionManager = Depends()
):
    """Generate comprehensive security report"""
    generator = ReportGenerator()
    report = await generator.generate_report(org_id, scan_id)
    return report