import pytest


@pytest.mark.asyncio
async def test_calc_success(client):
    payload = {
        "materials": [
            {"name": "steel", "qty": 10, "price_rub": 50.0},
            {"name": "copper", "qty": 2, "price_rub": 100.0},
        ]
    }

    response = await client.post("/calc", json=payload)

    assert response.status_code == 200
    assert response.json()["total_cost_rub"] == 700.0

@pytest.mark.asyncio
async def test_calc_validation_error(client):
    payload = {
        "materials": [
            {"name": "steel", "qty": -1, "price_rub": 50.0},
        ]
    }

    response = await client.post("/calc", json=payload)

    assert response.status_code == 422
