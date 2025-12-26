from db.models import CalcResult
from db.session import AsyncSessionLocal
from fastapi import APIRouter, Depends
from schemas.calc import CalcRequest, CalcResponse

from services.calculator import calculate_total_cost
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@router.post("/calc", response_model=CalcResponse)
async def calculate(
    data: CalcRequest,
    db: AsyncSession = Depends(get_db),
):
    total_cost = calculate_total_cost(data)

    result = CalcResult(total_cost_rub=total_cost)
    db.add(result)
    await db.commit()

    return {"total_cost_rub": float(total_cost)}
