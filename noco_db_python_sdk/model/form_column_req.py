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


class FormColumnReq(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Form Column Request
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def description() -> typing.Type['TextOrNull']:
                return TextOrNull
        
            @staticmethod
            def help() -> typing.Type['TextOrNull']:
                return TextOrNull
        
            @staticmethod
            def label() -> typing.Type['TextOrNull']:
                return TextOrNull
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            order = schemas.NumberSchema
        
            @staticmethod
            def required() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def show() -> typing.Type['ModelBool']:
                return ModelBool
            __annotations__ = {
                "description": description,
                "help": help,
                "label": label,
                "meta": meta,
                "order": order,
                "required": required,
                "show": show,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["help"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["label"]) -> 'TextOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "help", "label", "meta", "order", "required", "show", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["help"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> typing.Union['TextOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "help", "label", "meta", "order", "required", "show", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        help: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        label: typing.Union['TextOrNull', schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        required: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        show: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FormColumnReq':
        return super().__new__(
            cls,
            *args,
            description=description,
            help=help,
            label=label,
            meta=meta,
            order=order,
            required=required,
            show=show,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.meta import Meta
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.text_or_null import TextOrNull
