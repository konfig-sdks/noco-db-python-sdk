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


class Lookup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Lookup
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def fk_column_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def fk_lookup_column_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def fk_relation_column_id() -> typing.Type['Id']:
                return Id
            order = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "fk_column_id": fk_column_id,
                "fk_lookup_column_id": fk_lookup_column_id,
                "fk_relation_column_id": fk_relation_column_id,
                "order": order,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_lookup_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "fk_column_id", "fk_lookup_column_id", "fk_relation_column_id", "order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_lookup_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "fk_column_id", "fk_lookup_column_id", "fk_relation_column_id", "order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        fk_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        fk_lookup_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        fk_relation_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Lookup':
        return super().__new__(
            cls,
            *args,
            id=id,
            fk_column_id=fk_column_id,
            fk_lookup_column_id=fk_lookup_column_id,
            fk_relation_column_id=fk_relation_column_id,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.id import Id
