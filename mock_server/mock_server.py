# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import logging

import grpc

from grpc_core.protos import service_pb2_grpc, service_pb2
from settings import settings
from .raw_data import countries


def db_get_countries():
    return [Countries(**c) for c in countries]


def db_get_country_by_id(id: int):
    return [Countries(**c) for c in countries if c["id"] == id]


class Countries(service_pb2_grpc.CountriesServicer):
    async def GetCountry(
        self,
        request: service_pb2.GetCountryRequest,
        context: grpc.aio.ServicerContext,
    ) -> service_pb2.GetCountryResponse:
        return service_pb2.Country(message=db_get_countries())

    async def GetCountryByID(
        self,
        request: service_pb2.GetCountryByIDRequest,
        context: grpc.aio.ServicerContext,
    ) -> service_pb2.GetCountryByIDResponse:
        return service_pb2.Country(message=db_get_country_by_id(request.id))


async def serve() -> None:
    server = grpc.aio.server()
    service_pb2_grpc.add_CountriesServicer_to_server(Countries(), server)
    listen_addr = settings.secondary_addr
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
