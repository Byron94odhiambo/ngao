from sqlalchemy.ext.asyncio import AsyncSession
from app.models.organization import Organization
from app.models.user import User
from app.services.auth.auth_service import AuthService
from datetime import datetime

async def init_db(async_session: AsyncSession):
    try:
        async with async_session() as db:
            # Check if test organization already exists
            test_org = Organization(
                name="Tech Solutions Kenya",
                industry="Technology",
                size=25,
                subscription_tier="basic",
                contact_email="admin@techsolutions.co.ke",
                phone_number="+254712345678",
                created_at=datetime.utcnow()
            )
            db.add(test_org)
            await db.flush()

            # Create admin user
            auth_service = AuthService(db)
            hashed_password = auth_service.pwd_context.hash("securepassword123")
            
            admin_user = User(
                email="admin@techsolutions.co.ke",
                hashed_password=hashed_password,
                full_name="John Doe",
                phone_number="+254712345678",
                role="admin",
                organization_id=test_org.id,
                is_active=True,
                created_at=datetime.utcnow()
            )
            db.add(admin_user)
            await db.commit()
            print("Database initialized with test organization and admin user!")
            
    except Exception as e:
        print(f"Error initializing database: {str(e)}")
        raise
