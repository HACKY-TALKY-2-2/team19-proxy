from fastapi import APIRouter, status

from db import session_scope
from device.repositories import DeviceSQLRepository
from device.schemas import (
    CheckDeviceInCameraSchema,
    CreateDeviceSchema,
    UpdateDevicePositionSchema,
)

router = APIRouter()


@router.get("/devices")
async def list_devices():
    return [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ]


@router.get("/devices/{device_token}")
async def get_device(device_token: str):
    with session_scope() as session:
        device = DeviceSQLRepository(session=session).get_device_by_device_token(
            device_token=device_token,
        )
    return device


@router.post("/devices", status_code=status.HTTP_201_CREATED)
async def create_device(
    device: CreateDeviceSchema,
) -> dict[str, str]:
    with session_scope() as session:
        DeviceSQLRepository(session=session).create_device(
            device_token=device.device_token,
        )
    return {"detail": "success"}


@router.put("/devices/{device_token}/position")
async def update_device_position(
    device_token: str,
    position: UpdateDevicePositionSchema,
) -> dict[str, str]:
    with session_scope() as session:
        DeviceSQLRepository(session=session).update_device_position(
            device_token=device_token,
            longitude=position.longitude,
            latitude=position.latitude,
        )

    return {"detail": "success"}


@router.post("/devices/{device_token}/check-camera")
async def check_device_in_camera(
    device_token: str,
    position: CheckDeviceInCameraSchema,
) -> dict[str, bool]:
    with session_scope() as session:
        device = DeviceSQLRepository(session=session).get_device_by_device_token(
            device_token=device_token,
        )
        old_distance = DeviceSQLRepository(
            session=session
        ).get_closest_camera_to_position(
            longitude=device["longitude"],
            latitude=device["latitude"],
        )[
            "distance"
        ]
        new_distance = DeviceSQLRepository(
            session=session
        ).get_closest_camera_to_position(
            longitude=position.longitude,
            latitude=position.latitude,
        )[
            "distance"
        ]

    return {
        "entry_status": old_distance > 10 >= new_distance,
    }
