from fastapi import APIRouter

router = APIRouter()


@router.get("/devices")
async def list_devices():
    return [
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ]
