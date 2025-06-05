from datetime import date

import pytest

BOOKINGS_ENDPOINT = "/bookings/"
ROOMS_ENDPOINT = "/rooms/"


@pytest.mark.asyncio
async def test_create_booking(client):
    room_resp = await client.post(
        ROOMS_ENDPOINT, json={"description": "Room", "price": 100}
    )
    room_id = room_resp.json()["id"]

    booking_data = {
        "room_id": room_id,
        "start_date": str(date.today()),
        "end_date": str(date.today()),
    }
    response = await client.post(BOOKINGS_ENDPOINT, json=booking_data)
    assert response.status_code == 200
    data = response.json()
    assert data["room_id"] == room_id


@pytest.mark.asyncio
async def test_booking_overlap(client):
    room_resp = await client.post(
        ROOMS_ENDPOINT, json={"description": "Room", "price": 100}
    )
    room_id = room_resp.json()["id"]
    payload = {"room_id": room_id, "start_date": "2025-06-10", "end_date": "2025-06-15"}
    await client.post(BOOKINGS_ENDPOINT, json=payload)
    overlap_resp = await client.post(BOOKINGS_ENDPOINT, json=payload)
    assert overlap_resp.status_code == 400
    assert "already booked" in overlap_resp.json()["detail"]


@pytest.mark.asyncio
async def test_delete_booking(client):
    room_resp = await client.post(
        ROOMS_ENDPOINT, json={"description": "Room", "price": 100}
    )
    room_id = room_resp.json()["id"]
    payload = {"room_id": room_id, "start_date": "2025-06-10", "end_date": "2025-06-12"}
    booking_resp = await client.post(BOOKINGS_ENDPOINT, json=payload)
    booking_id = booking_resp.json()["id"]

    del_resp = await client.delete(f"{BOOKINGS_ENDPOINT}{booking_id}")
    assert del_resp.status_code == 204
