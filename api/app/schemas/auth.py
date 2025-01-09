from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import re

# Custom validator for Kenyan phone numbers
def validate_phone(phone: str) -> str:
    if not re.match(r'^\+254\d{9}$', phone):
        raise ValueError('Invalid Kenyan phone number')
    return phone

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    phone_number: str = Field(..., description="Kenyan phone number", pattern=r'^\+254\d{9}$')

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)
    role: str = 'admin'

class User(UserBase):
    id: int
    organization_id: int
    is_active: bool
    last_login: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True

class OrganizationBase(BaseModel):
    name: str
    industry: str
    size: int = Field(gt=0)
    subscription_tier: str = Field(..., pattern='^(basic|standard)$')
    contact_email: EmailStr
    phone_number: str = Field(..., pattern=r'^\+254\d{9}$')

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class OrganizationRegistration(BaseModel):
    organization: OrganizationCreate
    admin: UserCreate

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None
    exp: Optional[int] = None
