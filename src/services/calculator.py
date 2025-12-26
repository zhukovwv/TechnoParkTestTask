from sqlalchemy.ext.asyncio import AsyncSession

from db.models import CalcResult
from schemas.calc import Material


def calculate_total_cost(materials: list[Material]) -> float:
    return sum(m.qty * m.price_rub for m in materials)


async def save_calc_result(
    db: AsyncSession,
    total_cost: float,
) -> None:
    result = CalcResult(total_cost_rub=total_cost)
    db.add(result)
    await db.commit()
