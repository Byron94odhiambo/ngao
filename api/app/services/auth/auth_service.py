from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import jwt
from passlib.context import CryptContext
from app.models.user import User

class AuthService:
    SECRET_KEY = "ngao-security-platform-secret-key-2025"
    ALGORITHM = "HS256"

    def __init__(self, db: AsyncSession):
        self.db = db
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        try:
            query = select(User).where(User.email == email)
            result = await self.db.execute(query)
            user = result.scalar_one_or_none()

            if not user:
                print(f"User not found: {email}")
                return None
            if not self.verify_password(password, user.hashed_password):
                print("Invalid password")
                return None

            print(f"Authentication successful for user: {email}")
            return user
        except Exception as e:
            print(f"Authentication error: {str(e)}")
            return None

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
