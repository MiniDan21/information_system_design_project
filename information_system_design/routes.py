from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from grpc.aio import AioRpcError

from information_system_design import calculate, schemas


router = APIRouter(prefix="/api")


@router.get("/all")
async def get_all():
    try:
        countries = await calculate.calculate_with_all()
    except AioRpcError as e:
        raise HTTPException(status_code=404, detail=e.details())
    return JSONResponse(countries)


@router.get("/several")
async def get_several_by_id(id_list: schemas.ListIDRequest):
    try:
        country = await calculate.calculate_with_several(id_list)
    except AioRpcError as e:
        raise HTTPException(status_code=404, detail=e.details())
    return JSONResponse(country)
