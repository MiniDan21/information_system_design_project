import uuid
from enum import Enum
from typing import List
from pydantic import BaseModel


class Country(BaseModel):
    id: int
    countryName: str
    population: int
    area: int
    languages: List[str]
    gdp: int = None


class GetCountryRequest(BaseModel):
    pass


class GetCountryResponse(BaseModel):
    country: List[Country] = None


class GetCountryByIDRequest(BaseModel):
    id: int


class GetCountryByIDResponse(BaseModel):
    country: Country = None
