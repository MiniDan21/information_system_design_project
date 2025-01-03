from typing import Any

from fastapi import APIRouter, Depends


router = APIRouter(prefix="/api")


@router.get("/")
def list_countries(client: Any = Depends()):
    try:
        countries = await client.ListOrders(order_pb2.ListOrdersRequest())
    except AioRpcError as e:
        raise HTTPException(status_code=404, detail=e.details())

    return JSONResponse(OrderListResponse(**MessageToDict(orders)).dict())
