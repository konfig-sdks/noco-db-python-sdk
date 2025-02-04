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


class DbTableDuplicateTablePostRequestOptions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            excludeData = schemas.BoolSchema
            excludeViews = schemas.BoolSchema
            excludeHooks = schemas.BoolSchema
            __annotations__ = {
                "excludeData": excludeData,
                "excludeViews": excludeViews,
                "excludeHooks": excludeHooks,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeData"]) -> MetaOapg.properties.excludeData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeViews"]) -> MetaOapg.properties.excludeViews: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["excludeHooks"]) -> MetaOapg.properties.excludeHooks: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["excludeData", "excludeViews", "excludeHooks", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeData"]) -> typing.Union[MetaOapg.properties.excludeData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeViews"]) -> typing.Union[MetaOapg.properties.excludeViews, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["excludeHooks"]) -> typing.Union[MetaOapg.properties.excludeHooks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["excludeData", "excludeViews", "excludeHooks", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        excludeData: typing.Union[MetaOapg.properties.excludeData, bool, schemas.Unset] = schemas.unset,
        excludeViews: typing.Union[MetaOapg.properties.excludeViews, bool, schemas.Unset] = schemas.unset,
        excludeHooks: typing.Union[MetaOapg.properties.excludeHooks, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DbTableDuplicateTablePostRequestOptions':
        return super().__new__(
            cls,
            *args,
            excludeData=excludeData,
            excludeViews=excludeViews,
            excludeHooks=excludeHooks,
            _configuration=_configuration,
            **kwargs,
        )
