from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Dict
from passlib.context import CryptContext
from app.models.organization import Organization
from app.models.user import User
from datetime import datetime

class OnboardingService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def register_organization(self, org_data: Dict, admin_data: Dict) -> Dict:
        try:
            # Check if organization already exists
            existing_org = await self.db.execute(
                select(Organization).where(Organization.name == org_data["name"])
            )
            if existing_org.scalar_one_or_none():
                raise ValueError(f"Organization with name '{org_data['name']}' already exists")

            # Check if admin email already exists
            existing_user = await self.db.execute(
                select(User).where(User.email == admin_data["email"])
            )
            if existing_user.scalar_one_or_none():
                raise ValueError(f"User with email '{admin_data['email']}' already exists")

            # Create organization
            org = Organization(
                name=org_data["name"],
                industry=org_data["industry"],
                size=org_data["size"],
                subscription_tier=org_data["subscription_tier"],
                contact_email=org_data["contact_email"],
                phone_number=org_data["phone_number"],
                created_at=datetime.utcnow()
            )
            self.db.add(org)
            await self.db.flush()

            # Create admin user
            hashed_password = self.pwd_context.hash(admin_data["password"])
            admin = User(
                email=admin_data["email"],
                hashed_password=hashed_password,
                full_name=admin_data["full_name"],
                phone_number=admin_data["phone_number"],
                role="admin",
                organization_id=org.id,
                created_at=datetime.utcnow()
            )
            self.db.add(admin)
            await self.db.commit()
            await self.db.refresh(admin)

            return {
                "success": True,
                "organization_id": org.id,
                "admin_id": admin.id,
                "message": "Organization and admin user registered successfully"
            }

        except ValueError as e:
            await self.db.rollback()
            raise ValueError(str(e))
        except Exception as e:
            await self.db.rollback()
            print(f"Registration error: {str(e)}")
            raise ValueError(f"Registration failed: {str(e)}")
