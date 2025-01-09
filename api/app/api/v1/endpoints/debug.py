from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.deps import get_db
from app.models.user import User

router = APIRouter()

@router.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    """Debug endpoint to list all users"""
    query = select(User)
    result = await db.execute(query)
    users = result.scalars().all()
    return [{"email": user.email, "id": user.id} for user in users]
