import grpc
from grpc_core.protos import service_pb2_grpc
from settings import settings


async def grpc_country_client():
    channel = grpc.aio.insecure_channel(
        settings.secondary_addr,
    )
    client = service_pb2_grpc.CountriesStub(channel)
    return client
