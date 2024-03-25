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


class Gallery(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Gallery
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            alias = schemas.StrSchema
            
            
            class columns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['GalleryColumn']:
                        return GalleryColumn
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['GalleryColumn'], typing.List['GalleryColumn']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'GalleryColumn':
                    return super().__getitem__(i)
            cover_image = schemas.StrSchema
            cover_image_idx = schemas.IntSchema
        
            @staticmethod
            def deleted() -> typing.Type['ModelBool']:
                return ModelBool
        
            @staticmethod
            def fk_cover_image_col_id() -> typing.Type['StringOrNull']:
                return StringOrNull
            fk_model_id = schemas.StrSchema
            fk_view_id = schemas.StrSchema
            
            
            class lock_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
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
            def next_enabled() -> typing.Type['ModelBool']:
                return ModelBool
            order = schemas.NumberSchema
        
            @staticmethod
            def prev_enabled() -> typing.Type['ModelBool']:
                return ModelBool
            restrict_number = schemas.StrSchema
            restrict_size = schemas.StrSchema
            restrict_types = schemas.StrSchema
            __annotations__ = {
                "title": title,
                "alias": alias,
                "columns": columns,
                "cover_image": cover_image,
                "cover_image_idx": cover_image_idx,
                "deleted": deleted,
                "fk_cover_image_col_id": fk_cover_image_col_id,
                "fk_model_id": fk_model_id,
                "fk_view_id": fk_view_id,
                "lock_type": lock_type,
                "next_enabled": next_enabled,
                "order": order,
                "prev_enabled": prev_enabled,
                "restrict_number": restrict_number,
                "restrict_size": restrict_size,
                "restrict_types": restrict_types,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alias"]) -> MetaOapg.properties.alias: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_image"]) -> MetaOapg.properties.cover_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cover_image_idx"]) -> MetaOapg.properties.cover_image_idx: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_cover_image_col_id"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_model_id"]) -> MetaOapg.properties.fk_model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_view_id"]) -> MetaOapg.properties.fk_view_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lock_type"]) -> MetaOapg.properties.lock_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_enabled"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prev_enabled"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrict_number"]) -> MetaOapg.properties.restrict_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrict_size"]) -> MetaOapg.properties.restrict_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["restrict_types"]) -> MetaOapg.properties.restrict_types: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "alias", "columns", "cover_image", "cover_image_idx", "deleted", "fk_cover_image_col_id", "fk_model_id", "fk_view_id", "lock_type", "next_enabled", "order", "prev_enabled", "restrict_number", "restrict_size", "restrict_types", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alias"]) -> typing.Union[MetaOapg.properties.alias, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> typing.Union[MetaOapg.properties.columns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_image"]) -> typing.Union[MetaOapg.properties.cover_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cover_image_idx"]) -> typing.Union[MetaOapg.properties.cover_image_idx, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_cover_image_col_id"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_model_id"]) -> typing.Union[MetaOapg.properties.fk_model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_view_id"]) -> typing.Union[MetaOapg.properties.fk_view_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lock_type"]) -> typing.Union[MetaOapg.properties.lock_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_enabled"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prev_enabled"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrict_number"]) -> typing.Union[MetaOapg.properties.restrict_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrict_size"]) -> typing.Union[MetaOapg.properties.restrict_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["restrict_types"]) -> typing.Union[MetaOapg.properties.restrict_types, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "alias", "columns", "cover_image", "cover_image_idx", "deleted", "fk_cover_image_col_id", "fk_model_id", "fk_view_id", "lock_type", "next_enabled", "order", "prev_enabled", "restrict_number", "restrict_size", "restrict_types", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        alias: typing.Union[MetaOapg.properties.alias, str, schemas.Unset] = schemas.unset,
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, schemas.Unset] = schemas.unset,
        cover_image: typing.Union[MetaOapg.properties.cover_image, str, schemas.Unset] = schemas.unset,
        cover_image_idx: typing.Union[MetaOapg.properties.cover_image_idx, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        deleted: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        fk_cover_image_col_id: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        fk_model_id: typing.Union[MetaOapg.properties.fk_model_id, str, schemas.Unset] = schemas.unset,
        fk_view_id: typing.Union[MetaOapg.properties.fk_view_id, str, schemas.Unset] = schemas.unset,
        lock_type: typing.Union[MetaOapg.properties.lock_type, str, schemas.Unset] = schemas.unset,
        next_enabled: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        prev_enabled: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        restrict_number: typing.Union[MetaOapg.properties.restrict_number, str, schemas.Unset] = schemas.unset,
        restrict_size: typing.Union[MetaOapg.properties.restrict_size, str, schemas.Unset] = schemas.unset,
        restrict_types: typing.Union[MetaOapg.properties.restrict_types, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Gallery':
        return super().__new__(
            cls,
            *args,
            title=title,
            alias=alias,
            columns=columns,
            cover_image=cover_image,
            cover_image_idx=cover_image_idx,
            deleted=deleted,
            fk_cover_image_col_id=fk_cover_image_col_id,
            fk_model_id=fk_model_id,
            fk_view_id=fk_view_id,
            lock_type=lock_type,
            next_enabled=next_enabled,
            order=order,
            prev_enabled=prev_enabled,
            restrict_number=restrict_number,
            restrict_size=restrict_size,
            restrict_types=restrict_types,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.gallery_column import GalleryColumn
from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull