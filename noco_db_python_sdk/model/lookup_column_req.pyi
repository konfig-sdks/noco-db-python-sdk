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


class LookupColumnReq(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Lookup Column Request
    """


    class MetaOapg:
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def fk_lookup_column_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def fk_relation_column_id() -> typing.Type['Id']:
                return Id
            
            
            class uidt(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LOOKUP(cls):
                    return cls("Lookup")
            __annotations__ = {
                "title": title,
                "fk_lookup_column_id": fk_lookup_column_id,
                "fk_relation_column_id": fk_relation_column_id,
                "uidt": uidt,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_lookup_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uidt"]) -> MetaOapg.properties.uidt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "fk_lookup_column_id", "fk_relation_column_id", "uidt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_lookup_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_relation_column_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uidt"]) -> typing.Union[MetaOapg.properties.uidt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "fk_lookup_column_id", "fk_relation_column_id", "uidt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        fk_lookup_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        fk_relation_column_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        uidt: typing.Union[MetaOapg.properties.uidt, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LookupColumnReq':
        return super().__new__(
            cls,
            *args,
            title=title,
            fk_lookup_column_id=fk_lookup_column_id,
            fk_relation_column_id=fk_relation_column_id,
            uidt=uidt,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.id import Id
