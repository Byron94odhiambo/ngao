from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from datetime import datetime

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey("assets.id"))
    scan_type = Column(String)  # vulnerability, network, ssl, etc.
    status = Column(String)  # completed, failed, in_progress
    findings = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)

    # Relationship
    asset = relationship("Asset", back_populates="scan_results")
