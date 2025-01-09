# NGAO Security Platform

NGAO (Next Generation Asset Observer) is a comprehensive cybersecurity platform designed for your asset security management, focusing on vulnerability assessment, compliance monitoring, and security scanning.

## Features

### Core Features
- [x] User Authentication & Authorization
- [x] Organization Management
- [x] Asset Management
- [x] Basic Vulnerability Scanning
- [ ] Compliance Monitoring
- [ ] Reporting System

### Security Scanning
- [x] Network vulnerability scanning
- [x] SSL certificate verification
- [x] Common vulnerability checks
- [ ] Password security assessment
- [ ] Mobile money security checks
- [ ] Real-time monitoring

### Compliance Features
- [ ] Data Protection Act (2019) compliance checks
- [ ] Basic security policy templates
- [ ] Compliance reports generation
- [ ] Risk assessment
- [ ] Audit logs

### Notification System
- [ ] Email notifications
- [ ] SMS alerts (Africa's Talking integration)
- [ ] Custom alert rules
- [ ] Alert priority levels

## Technical Stack

- Backend: FastAPI (Python)
- Database: PostgreSQL
- Authentication: JWT
- Containerization: Docker
- Infrastructure: Docker Compose

## Installation

1. Clone the repository:
```bash
git clone git@github.com:yourusername/ngao.git
cd ngao
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Build and start the containers:
```bash
docker-compose build
docker-compose up -d
```

4. Initialize the database:
```bash
# Database migrations and initial data are handled automatically on startup
```

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - User login
- [ ] `POST /api/v1/auth/refresh` - Refresh token
- [ ] `POST /api/v1/auth/logout` - User logout

### Assets
- `POST /api/v1/assets` - Create new asset
- `GET /api/v1/assets` - List assets
- [ ] `GET /api/v1/assets/{id}` - Get asset details
- [ ] `PUT /api/v1/assets/{id}` - Update asset
- [ ] `DELETE /api/v1/assets/{id}` - Delete asset

### Scanning
- `POST /api/v1/scanning/{asset_id}/scan` - Start new scan
- [ ] `GET /api/v1/scanning/{scan_id}/results` - Get scan results
- [ ] `GET /api/v1/scanning/history` - View scan history
- [ ] `GET /api/v1/scanning/metrics` - Get scanning metrics

### Compliance
- [ ] `GET /api/v1/compliance/status` - Get compliance status
- [ ] `POST /api/v1/compliance/check` - Run compliance check
- [ ] `GET /api/v1/compliance/reports` - Get compliance reports

## TODO List

### Priority 1 (Core Features)
1. Add user management
   - User roles (Admin, Security Officer, Analyst)
   - Role-based access control
   - Password reset functionality

2. Enhance scanning capabilities
   - Add more vulnerability checks
   - Implement scan scheduling
   - Add scan configuration options
   - Real-time scan progress updates

3. Implement compliance monitoring
   - DPA 2019 compliance checks
   - Basic security policy templates
   - Compliance reporting

### Priority 2 (Enhanced Features)
1. Reporting system
   - PDF report generation
   - CSV export
   - Custom report templates
   - Scheduled reports

2. Notification system
   - Email notifications
   - SMS integration
   - Custom alert rules
   - Alert management

3. Dashboard and analytics
   - Security metrics
   - Trend analysis
   - Risk scoring
   - Asset health monitoring

### Priority 3 (Advanced Features)
1. Advanced security features
   - Automated remediation suggestions
   - Integration with security tools
   - Threat intelligence feeds
   - Custom scanning rules

2. Mobile app development
   - Real-time alerts
   - Basic dashboard
   - Scan management
   - Report viewing

3. API integrations
   - SIEM integration
   - Ticketing system integration
   - Cloud provider integrations
   - Custom webhook support

## Subscription Tiers

### Basic Tier (1-50 employees)
- [x] Monthly network scans
- [x] Basic compliance checks
- [x] Email reports
- [ ] Basic dashboard access

### Standard Tier (50+ employees)
- [ ] Weekly scans
- [ ] Full compliance monitoring
- [ ] SMS + Email alerts
- [ ] Advanced reporting
- [ ] Custom scan rules
- [ ] API access

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## Acknowledgments
- FastAPI
- SQLAlchemy
- Python-Nmap
- Africa's Talking API