# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from noco_db_python_sdk import schemas  # noqa: F401


class TableRecordsReadByIdResponseJson(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            name = schemas.StrSchema
            age = schemas.NumberSchema
            email = schemas.StrSchema
            isSubscribed = schemas.BoolSchema
        
            @staticmethod
            def address() -> typing.Type['TableRecordsReadByIdResponseJsonAddress']:
                return TableRecordsReadByIdResponseJsonAddress
        
            @staticmethod
            def hobbies() -> typing.Type['TableRecordsReadByIdResponseJsonHobbies']:
                return TableRecordsReadByIdResponseJsonHobbies
        
            @staticmethod
            def scores() -> typing.Type['TableRecordsReadByIdResponseJsonScores']:
                return TableRecordsReadByIdResponseJsonScores
            __annotations__ = {
                "name": name,
                "age": age,
                "email": email,
                "isSubscribed": isSubscribed,
                "address": address,
                "hobbies": hobbies,
                "scores": scores,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age"]) -> MetaOapg.properties.age: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSubscribed"]) -> MetaOapg.properties.isSubscribed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'TableRecordsReadByIdResponseJsonAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hobbies"]) -> 'TableRecordsReadByIdResponseJsonHobbies': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scores"]) -> 'TableRecordsReadByIdResponseJsonScores': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "age", "email", "isSubscribed", "address", "hobbies", "scores", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age"]) -> typing.Union[MetaOapg.properties.age, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSubscribed"]) -> typing.Union[MetaOapg.properties.isSubscribed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['TableRecordsReadByIdResponseJsonAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hobbies"]) -> typing.Union['TableRecordsReadByIdResponseJsonHobbies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scores"]) -> typing.Union['TableRecordsReadByIdResponseJsonScores', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "age", "email", "isSubscribed", "address", "hobbies", "scores", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        age: typing.Union[MetaOapg.properties.age, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        isSubscribed: typing.Union[MetaOapg.properties.isSubscribed, bool, schemas.Unset] = schemas.unset,
        address: typing.Union['TableRecordsReadByIdResponseJsonAddress', schemas.Unset] = schemas.unset,
        hobbies: typing.Union['TableRecordsReadByIdResponseJsonHobbies', schemas.Unset] = schemas.unset,
        scores: typing.Union['TableRecordsReadByIdResponseJsonScores', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TableRecordsReadByIdResponseJson':
        return super().__new__(
            cls,
            *args,
            name=name,
            age=age,
            email=email,
            isSubscribed=isSubscribed,
            address=address,
            hobbies=hobbies,
            scores=scores,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.table_records_read_by_id_response_json_address import TableRecordsReadByIdResponseJsonAddress
from noco_db_python_sdk.model.table_records_read_by_id_response_json_hobbies import TableRecordsReadByIdResponseJsonHobbies
from noco_db_python_sdk.model.table_records_read_by_id_response_json_scores import TableRecordsReadByIdResponseJsonScores