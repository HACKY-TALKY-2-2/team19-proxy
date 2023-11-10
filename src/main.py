from fastapi import FastAPI

from device.apis import router as device_router
from proxy.apis import router as proxy_router

app = FastAPI()
app.include_router(device_router)
app.include_router(proxy_router)
