"""Модуль обращения к gRPC"""

from typing import Any
from google.protobuf.json_format import MessageToDict

from grpc_core.clients.country import grpc_country_client
from grpc_core.protos import service_pb2
from grpc_core.servers import schemas

from .schemas import ListIDRequest

[
    "ByteSize",
    "Clear",
    "ClearExtension",
    "ClearField",
    "CopyFrom",
    "DESCRIPTOR",
    "DiscardUnknownFields",
    "Extensions",
    "FindInitializationErrors",
    "FromString",
    "HasExtension",
    "HasField",
    "IsInitialized",
    "ListFields",
    "MergeFrom",
    "MergeFromString",
    "ParseFromString",
    "SerializePartialToString",
    "SerializeToString",
    "SetInParent",
    "UnknownFields",
    "WhichOneof",
    "_CheckCalledFromGeneratedFile",
    "_ListFieldsItemKey",
    "_SetListener",
    "__class__",
    "__contains__",
    "__deepcopy__",
    "__delattr__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getstate__",
    "__gt__",
    "__hash__",
    "__init__",
    "__init_subclass__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__setstate__",
    "__sizeof__",
    "__slots__",
    "__str__",
    "__subclasshook__",
    "__unicode__",
]


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
