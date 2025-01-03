import pytest
import pytest_asyncio
from google.protobuf.json_format import MessageToDict

from grpc_core.clients.country import grpc_country_client
from grpc_core.protos import service_pb2
from grpc_core.servers import schemas
from .assets.py_data import countries


class TestGRPC:
    @pytest_asyncio.fixture(autouse=True)
    async def setup(self):
        self.client = await grpc_country_client()

    @pytest.mark.asyncio
    async def test__get_country__raw_data(self, launch_server):
        self.client = await grpc_country_client()
        new_countries = await self.client.GetCountry(service_pb2.GetCountryRequest())
        new_countries = schemas.GetCountryResponse(
            **MessageToDict(new_countries)
        ).model_dump()["country"]

        assert len(new_countries) == len(countries), "Lengths of structures not equal"
        assert (
            new_countries[0]["countryName"] == countries[0]["country_name"]
        ), "The country names of first elements not same"

    @pytest.mark.asyncio
    @pytest.mark.parametrize("id", list(range(1, 11)))
    async def test__get_country_by_id__raw_data(self, launch_server, id):
        self.client = await grpc_country_client()
        new_country = await self.client.GetCountryByID(
            service_pb2.GetCountryByIDRequest(id=id)
        )
        new_country = schemas.GetCountryByIDResponse(
            **MessageToDict(new_country)
        ).model_dump()["country"]
        print(new_country)
        assert (
            new_country["countryName"] == countries[id - 1]["country_name"]
        ), "The country names of mapped elements not same"
