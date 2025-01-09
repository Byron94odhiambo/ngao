# api/app/services/mobile_money/mpesa_checker.py
class MPESASecurityChecker:
    """M-PESA integration security checker"""
    
    async def check_integration_security(self, org_id: int) -> Dict:
        """Check M-PESA integration security settings"""
        checks = {
            'api_security': self._check_api_security(org_id),
            'transaction_monitoring': self._check_transaction_monitoring(org_id),
            'authentication': self._check_authentication(org_id),
            'callback_security': self._check_callback_security(org_id)
        }
        
        return {
            'status': 'completed',
            'results': checks,
            'recommendations': self._generate_recommendations(checks)
        }