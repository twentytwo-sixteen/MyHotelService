import pytest

ROOMS_ENDPOINT = "/rooms/"


@pytest.mark.asyncio
async def test_create_room(client):
    response = await client.post(
        ROOMS_ENDPOINT, json={"description": "Test Room", "price": 100}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Test Room"
    assert data["price"] == 100


@pytest.mark.asyncio
async def test_get_rooms(client):
    await client.post(ROOMS_ENDPOINT, json={"description": "Room A", "price": 50})
    await client.post(ROOMS_ENDPOINT, json={"description": "Room B", "price": 150})
    response = await client.get(ROOMS_ENDPOINT)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2
