# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x07\x63ountry\"z\n\x07\x43ountry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x14\n\x0c\x63ountry_name\x18\x02 \x01(\t\x12\x12\n\npopulation\x18\x03 \x01(\x05\x12\x0c\n\x04\x61rea\x18\x04 \x01(\x05\x12\x11\n\tlanguages\x18\x05 \x03(\t\x12\x10\n\x03gdp\x18\x06 \x01(\x05H\x00\x88\x01\x01\x42\x06\n\x04_gdp\"\x13\n\x11GetCountryRequest\"7\n\x12GetCountryResponse\x12!\n\x07\x63ountry\x18\x01 \x03(\x0b\x32\x10.country.Country\"#\n\x15GetCountryByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"L\n\x16GetCountryByIDResponse\x12&\n\x07\x63ountry\x18\x01 \x01(\x0b\x32\x10.country.CountryH\x00\x88\x01\x01\x42\n\n\x08_country2\xa5\x01\n\tCountries\x12\x45\n\nGetCountry\x12\x1a.country.GetCountryRequest\x1a\x1b.country.GetCountryResponse\x12Q\n\x0eGetCountryByID\x12\x1e.country.GetCountryByIDRequest\x1a\x1f.country.GetCountryByIDResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_COUNTRY']._serialized_start=26
  _globals['_COUNTRY']._serialized_end=148
  _globals['_GETCOUNTRYREQUEST']._serialized_start=150
  _globals['_GETCOUNTRYREQUEST']._serialized_end=169
  _globals['_GETCOUNTRYRESPONSE']._serialized_start=171
  _globals['_GETCOUNTRYRESPONSE']._serialized_end=226
  _globals['_GETCOUNTRYBYIDREQUEST']._serialized_start=228
  _globals['_GETCOUNTRYBYIDREQUEST']._serialized_end=263
  _globals['_GETCOUNTRYBYIDRESPONSE']._serialized_start=265
  _globals['_GETCOUNTRYBYIDRESPONSE']._serialized_end=341
  _globals['_COUNTRIES']._serialized_start=344
  _globals['_COUNTRIES']._serialized_end=509
# @@protoc_insertion_point(module_scope)
