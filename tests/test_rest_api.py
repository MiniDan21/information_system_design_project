import json

import pytest
import httpx
from random import randint

from settings import settings
from .assets.py_data import countries


class TestRESTAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_url = "http://" + settings.main_addr + "/api"
        self.several_url = self.base_url + "/several"
        self.all_url = self.base_url + "/all"

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "ids", [tuple([randint(1, 10) for _ in range(randint(2, 5))]) for _ in range(3)]
    )
    async def test__api_several(self, ids):
        print(ids)
        json_data = {"list_id": ids}
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method="GET", url=self.several_url, content=json.dumps(json_data)
            )
            assert response.status_code == 200, "Status code not 200"
            data = response.json()
            filtered_countries = [c for c in countries if c["id"] in ids]
            assert len(data) == len(
                filtered_countries
            ), "Lengths of structures not equal"
            assert (
                data[0]["countryName"] == filtered_countries[0]["country_name"]
            ), "The country names of first elements not same"

    @pytest.mark.asyncio
    async def test__api_all(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.all_url)
            assert response.status_code == 200, "Status code not 200"
            data = response.json()
            assert len(data) == len(countries), "Lengths of structures not equal"
            assert (
                data[0]["countryName"] == countries[0]["country_name"]
            ), "The country names of first elements not same"
