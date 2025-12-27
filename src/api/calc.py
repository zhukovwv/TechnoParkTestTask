import structlog
from db.session import get_db
from fastapi import APIRouter, Depends
from schemas.calc import CalcRequest, CalcResponse
from services.calculator import calculate_total_cost, save_calc_result
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/calc", response_model=CalcResponse)
async def calc(
    data: CalcRequest,
    db: AsyncSession = Depends(get_db),
):
    logger = structlog.get_logger()

    logger.info("request_received", path="/calc", payload=data.model_dump())

    total = calculate_total_cost(data.materials)
    await save_calc_result(db, total)

    logger.info("calc_completed", result=total)

    return CalcResponse(total_cost_rub=total)

