from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, async_session
from app.models import Base
from app.api.v1.endpoints import assets, auth, scanning
from app.db.init_db import init_db

app = FastAPI(title="NGAO Security Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(assets.router, prefix="/api/v1/assets", tags=["assets"])
app.include_router(scanning.router, prefix="/api/v1/scanning", tags=["scanning"])

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await init_db(async_session)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
