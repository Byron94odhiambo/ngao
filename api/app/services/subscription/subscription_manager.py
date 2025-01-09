# api/app/services/subscription/subscription_manager.py
from datetime import datetime, timedelta
from typing import Dict

class SubscriptionManager:
    """Manages subscription tiers and scheduling"""
    
    def __init__(self):
        self.subscription_configs = {
            'basic': {
                'scan_frequency': 30,  # days
                'features': {
                    'network_scan': True,
                    'basic_compliance': True,
                    'email_reports': True,
                    'sms_notifications': False,
                    'mobile_money_checks': False,
                    'full_compliance': False
                },
                'max_assets': 10,
                'price_monthly': 10000  # KES
            },
            'standard': {
                'scan_frequency': 7,  # days
                'features': {
                    'network_scan': True,
                    'basic_compliance': True,
                    'email_reports': True,
                    'sms_notifications': True,
                    'mobile_money_checks': True,
                    'full_compliance': True
                },
                'max_assets': 50,
                'price_monthly': 25000  # KES
            }
        }
    
    async def get_next_scan_date(self, org_id: int) -> datetime:
        """Calculate next scan date based on subscription"""
        org = await self.get_organization(org_id)
        frequency = self.subscription_configs[org.subscription_tier]['scan_frequency']
        last_scan = org.last_scan_date or datetime.utcnow()
        return last_scan + timedelta(days=frequency)
    
    async def can_access_feature(self, org_id: int, feature: str) -> bool:
        """Check if organization can access a specific feature"""
        org = await self.get_organization(org_id)
        return self.subscription_configs[org.subscription_tier]['features'].get(feature, False)