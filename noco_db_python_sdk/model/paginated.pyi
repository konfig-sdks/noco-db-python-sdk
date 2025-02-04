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


class Paginated(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Paginated
    """


    class MetaOapg:
        
        class properties:
            isFirstPage = schemas.BoolSchema
            isLastPage = schemas.BoolSchema
            page = schemas.NumberSchema
            pageSize = schemas.NumberSchema
            totalRows = schemas.NumberSchema
            __annotations__ = {
                "isFirstPage": isFirstPage,
                "isLastPage": isLastPage,
                "page": page,
                "pageSize": pageSize,
                "totalRows": totalRows,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFirstPage"]) -> MetaOapg.properties.isFirstPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isLastPage"]) -> MetaOapg.properties.isLastPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pageSize"]) -> MetaOapg.properties.pageSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalRows"]) -> MetaOapg.properties.totalRows: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isFirstPage", "isLastPage", "page", "pageSize", "totalRows", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFirstPage"]) -> typing.Union[MetaOapg.properties.isFirstPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isLastPage"]) -> typing.Union[MetaOapg.properties.isLastPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> typing.Union[MetaOapg.properties.page, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pageSize"]) -> typing.Union[MetaOapg.properties.pageSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalRows"]) -> typing.Union[MetaOapg.properties.totalRows, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isFirstPage", "isLastPage", "page", "pageSize", "totalRows", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        isFirstPage: typing.Union[MetaOapg.properties.isFirstPage, bool, schemas.Unset] = schemas.unset,
        isLastPage: typing.Union[MetaOapg.properties.isLastPage, bool, schemas.Unset] = schemas.unset,
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        pageSize: typing.Union[MetaOapg.properties.pageSize, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalRows: typing.Union[MetaOapg.properties.totalRows, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Paginated':
        return super().__new__(
            cls,
            *args,
            isFirstPage=isFirstPage,
            isLastPage=isLastPage,
            page=page,
            pageSize=pageSize,
            totalRows=totalRows,
            _configuration=_configuration,
            **kwargs,
        )
