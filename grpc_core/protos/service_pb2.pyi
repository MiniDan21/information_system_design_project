from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = ("id", "country_name", "population", "area", "languages", "gdp")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    POPULATION_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    GDP_FIELD_NUMBER: _ClassVar[int]
    id: int
    country_name: str
    population: int
    area: int
    languages: _containers.RepeatedScalarFieldContainer[str]
    gdp: int
    def __init__(self, id: _Optional[int] = ..., country_name: _Optional[str] = ..., population: _Optional[int] = ..., area: _Optional[int] = ..., languages: _Optional[_Iterable[str]] = ..., gdp: _Optional[int] = ...) -> None: ...

class GetCountryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCountryResponse(_message.Message):
    __slots__ = ("country",)
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(self, country: _Optional[_Iterable[_Union[Country, _Mapping]]] = ...) -> None: ...

class GetCountryByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetCountryByIDResponse(_message.Message):
    __slots__ = ("country",)
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: Country
    def __init__(self, country: _Optional[_Union[Country, _Mapping]] = ...) -> None: ...
