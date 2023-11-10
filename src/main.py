from fastapi import FastAPI

from device.apis import router as device_router

app = FastAPI()
app.include_router(device_router)
