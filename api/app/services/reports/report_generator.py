# api/app/services/reports/report_generator.py
class ReportGenerator:
    """Generates comprehensive security reports"""
    
    async def generate_report(self, org_id: int, scan_id: int) -> Dict:
        """Generate detailed security report"""
        scan_result = await self.get_scan_result(scan_id)
        org = await self.get_organization(org_id)
        
        report = {
            'organization': {
                'name': org.name,
                'subscription_tier': org.subscription_tier
            },
            'scan_summary': await self._generate_scan_summary(scan_result),
            'vulnerabilities': await self._analyze_vulnerabilities(scan_result),
            'compliance_status': await self._check_compliance_status(org_id),
            'recommendations': await self._generate_recommendations(scan_result),
            'next_scan_date': await self._get_next_scan_date(org_id)
        }
        
        if org.subscription_tier == 'standard':
            report['mobile_money'] = await self._check_mobile_money_security(org_id)
            report['detailed_compliance'] = await self._generate_detailed_compliance(org_id)
        
        return report
    
    async def _generate_scan_summary(self, scan_result: Dict) -> Dict:
        """Generate executive summary of scan findings"""
        return {
            'total_vulnerabilities': len(scan_result.get('findings', [])),
            'risk_level': self._calculate_risk_level(scan_result),
            'critical_findings': self._get_critical_findings(scan_result),
            'scan_date': scan_result.get('scan_date')
        }