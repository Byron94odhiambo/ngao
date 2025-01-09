from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ip_address = Column(String)
    hostname = Column(String)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_scan = Column(DateTime)

    # Relationships
    organization = relationship("Organization", back_populates="assets")
    scan_results = relationship("ScanResult", back_populates="asset")

    def __repr__(self):
        return f"<Asset {self.name}>"
