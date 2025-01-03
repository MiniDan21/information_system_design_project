"""Модуль обращения к gRPC"""

from typing import Any
from google.protobuf.json_format import MessageToDict

from grpc_core.clients.country import grpc_country_client
from grpc_core.protos import service_pb2
from grpc_core.servers import schemas

from .schemas import ListIDRequest


async def use_calculate_with_all() -> dict[str, Any]:
    _client = await grpc_country_client()
    countries = await _client.GetCountry(service_pb2.GetCountryRequest())
    return schemas.GetCountryResponse(**MessageToDict(countries)).model_dump()[
        "country"
    ]


async def use_calculate_with_several(ids: ListIDRequest) -> dict[str, Any]:
    _client = await grpc_country_client()
    countries = schemas.GetCountryResponse(
        **MessageToDict(await _client.GetCountry(service_pb2.GetCountryRequest()))
    ).model_dump()
    countries = [c for c in countries["country"] if c["id"] in ids.list_id]
    return countries
