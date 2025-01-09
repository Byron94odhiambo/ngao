# api/app/models/audit_log.py
class AuditLog(Base):
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String, nullable=False)
    resource_type = Column(String)
    resource_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String)
    
    user = relationship("User", back_populates="audit_logs")