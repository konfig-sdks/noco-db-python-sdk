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


class View(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for View
    """


    class MetaOapg:
        required = {
            "show",
            "fk_model_id",
            "title",
            "type",
        }
        
        class properties:
            title = schemas.StrSchema
        
            @staticmethod
            def fk_model_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def show() -> typing.Type['ModelBool']:
                return ModelBool
            type = schemas.NumberSchema
        
            @staticmethod
            def source_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
            
            
            class lock_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "collaborative": "COLLABORATIVE",
                        "locked": "LOCKED",
                        "personal": "PERSONAL",
                    }
                
                @schemas.classproperty
                def COLLABORATIVE(cls):
                    return cls("collaborative")
                
                @schemas.classproperty
                def LOCKED(cls):
                    return cls("locked")
                
                @schemas.classproperty
                def PERSONAL(cls):
                    return cls("personal")
        
            @staticmethod
            def meta() -> typing.Type['Meta']:
                return Meta
            order = schemas.NumberSchema
        
            @staticmethod
            def password() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def base_id() -> typing.Type['Id']:
                return Id
        
            @staticmethod
            def show_system_fields() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def is_default() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def uuid() -> typing.Type['StringOrNull']:
                return StringOrNull
            
            
            class view(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Form,
                            Gallery,
                            Grid,
                            Kanban,
                            Map,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'view':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "title": title,
                "fk_model_id": fk_model_id,
                "show": show,
                "type": type,
                "source_id": source_id,
                "id": id,
                "lock_type": lock_type,
                "meta": meta,
                "order": order,
                "password": password,
                "base_id": base_id,
                "show_system_fields": show_system_fields,
                "is_default": is_default,
                "uuid": uuid,
                "view": view,
            }
    
    show: 'ModelBool'
    fk_model_id: 'Id'
    title: MetaOapg.properties.title
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_model_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_type"]) -> MetaOapg.properties.lock_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'Meta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["show_system_fields"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_default"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["view"]) -> MetaOapg.properties.view: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "fk_model_id", "show", "type", "source_id", "id", "lock_type", "meta", "order", "password", "base_id", "show_system_fields", "is_default", "uuid", "view", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_model_id"]) -> 'Id': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show"]) -> 'ModelBool': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_type"]) -> typing.Union[MetaOapg.properties.lock_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['Meta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["show_system_fields"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_default"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["view"]) -> typing.Union[MetaOapg.properties.view, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "fk_model_id", "show", "type", "source_id", "id", "lock_type", "meta", "order", "password", "base_id", "show_system_fields", "is_default", "uuid", "view", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        show: 'ModelBool',
        fk_model_id: 'Id',
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: typing.Union[MetaOapg.properties.type, decimal.Decimal, int, float, ],
        source_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        lock_type: typing.Union[MetaOapg.properties.lock_type, str, schemas.Unset] = schemas.unset,
        meta: typing.Union['Meta', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        password: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        base_id: typing.Union['Id', schemas.Unset] = schemas.unset,
        show_system_fields: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        is_default: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        uuid: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        view: typing.Union[MetaOapg.properties.view, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'View':
        return super().__new__(
            cls,
            *args,
            show=show,
            fk_model_id=fk_model_id,
            title=title,
            type=type,
            source_id=source_id,
            id=id,
            lock_type=lock_type,
            meta=meta,
            order=order,
            password=password,
            base_id=base_id,
            show_system_fields=show_system_fields,
            is_default=is_default,
            uuid=uuid,
            view=view,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.form import Form
from noco_db_python_sdk.model.gallery import Gallery
from noco_db_python_sdk.model.grid import Grid
from noco_db_python_sdk.model.id import Id
from noco_db_python_sdk.model.kanban import Kanban
from noco_db_python_sdk.model.map import Map
from noco_db_python_sdk.model.meta import Meta
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull