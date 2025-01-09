# api/app/services/scanners/network_scanner.py
import nmap
from typing import Dict, List
import ssl
import socket
from datetime import datetime

class NetworkScanner:
    def __init__(self):
        self.nmap_scanner = nmap.PortScanner()
    
    async def scan_network(self, target: str) -> Dict:
        """Comprehensive network scan including common vulnerabilities"""
        basic_scan = self.nmap_scanner.scan(
            target, 
            arguments='-sV --script=vuln,ssl-cert,http-security-headers'
        )
        
        ssl_results = await self.verify_ssl(target)
        password_policy = await self.check_password_policy(target)
        
        return {
            'timestamp': datetime.utcnow(),
            'basic_scan': basic_scan,
            'ssl_verification': ssl_results,
            'password_policy': password_policy
        }
    
    async def verify_ssl(self, target: str) -> Dict:
        """Verify SSL certificate and configuration"""
        try:
            context = ssl.create_default_context()
            with socket.create_connection((target, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=target) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    return {
                        'valid': True,
                        'cert_details': cert,
                        'cipher': cipher
                    }
        except Exception as e:
            return {'valid': False, 'error': str(e)}