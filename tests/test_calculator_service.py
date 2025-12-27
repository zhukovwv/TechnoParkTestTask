from schemas.calc import Material
from services.calculator import calculate_total_cost


def test_calculate_total_cost():
    materials = [
        Material(name="steel", qty=10, price_rub=5.0),
        Material(name="copper", qty=2, price_rub=20.0),
    ]

    result = calculate_total_cost(materials)

    assert result == 90.0
