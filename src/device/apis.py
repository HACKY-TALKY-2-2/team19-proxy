from fastapi import APIRouter, status

from db import session_scope
from device.repositories import DeviceSQLRepository
from device.schemas import CreateDeviceSchema

router = APIRouter()


@router.get("/devices")
async def list_devices():
    return [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ]


@router.post("/devices", status_code=status.HTTP_201_CREATED)
async def create_device(
    device: CreateDeviceSchema,
) -> dict[str, str]:
    with session_scope() as session:
        DeviceSQLRepository(session=session).create_device(
            device_token=device.device_token,
        )
    return {"detail": "success"}
