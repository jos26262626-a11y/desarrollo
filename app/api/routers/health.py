from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from sqlalchemy import text

router = APIRouter()

@router.get("")
async def health_check(db: AsyncSession = Depends(get_db)):
    await db.execute(text("SELECT 1"))
    return {"status": "ok - conectado a BD"}

