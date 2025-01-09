# api/app/services/notifications/sms_service.py
from typing import Dict
import httpx
from app.core.config import settings

class SMSService:
    """SMS notification service using Africa's Talking API"""
    
    def __init__(self):
        self.api_key = settings.AFRICASTALKING_API_KEY
        self.username = settings.AFRICASTALKING_USERNAME
        self.base_url = "https://api.africastalking.com/version1/messaging"
    
    async def send_notification(self, phone_number: str, message: str) -> Dict:
        """Send SMS notification"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                data={
                    'username': self.username,
                    'to': phone_number,
                    'message': message
                },
                headers={
                    'ApiKey': self.api_key,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            )
            return response.json()