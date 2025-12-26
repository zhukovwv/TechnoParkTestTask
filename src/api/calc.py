from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from schemas.calc import CalcRequest, CalcResponse
from services.calculator import calculate_total_cost, save_calc_result

router = APIRouter()


@router.post("/calc", response_model=CalcResponse)
async def calc(
    data: CalcRequest,
    db: AsyncSession = Depends(get_db),
):
    total = calculate_total_cost(data.materials)
    await save_calc_result(db, total)
    return CalcResponse(total_cost_rub=total)
