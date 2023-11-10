from fastapi import APIRouter
from httpx import URL, AsyncClient
from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import StreamingResponse

router = APIRouter()
client = AsyncClient(base_url="http://localhost:8080")


async def _reverse_proxy(request: Request):
    print(request.url.path)
    url = URL(
        path=request.url.path,
        query=request.url.query.encode("utf-8"),
    )
    rp_request = client.build_request(
        method=request.method,
        url=url,
        headers=request.headers.raw,
        content=request.stream(),
    )
    rp_response = await client.send(rp_request, stream=True)
    return StreamingResponse(
        content=rp_response.aiter_raw(),
        status_code=rp_response.status_code,
        headers=rp_response.headers,
        background=BackgroundTask(rp_response.aclose),
    )


router.add_route("/cameras", _reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])
router.add_route("/reports", _reverse_proxy, ["GET", "POST", "PUT", "PATCH", "DELETE"])
