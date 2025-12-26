from decimal import Decimal

from schemas.calc import CalcRequest


def calculate_total_cost(data: CalcRequest) -> Decimal:
    total = Decimal("0")

    for material in data.materials:
        total += Decimal(str(material.qty)) * Decimal(str(material.price_rub))

    return total
