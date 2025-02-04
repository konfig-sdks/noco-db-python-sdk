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


class BaseGetInfoByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Node = schemas.StrSchema
            Arch = schemas.StrSchema
            Platform = schemas.StrSchema
            Docker = schemas.BoolSchema
            Database = schemas.StrSchema
            ProjectOnRootDB = schemas.BoolSchema
            RootDB = schemas.StrSchema
            PackageVersion = schemas.StrSchema
            __annotations__ = {
                "Node": Node,
                "Arch": Arch,
                "Platform": Platform,
                "Docker": Docker,
                "Database": Database,
                "ProjectOnRootDB": ProjectOnRootDB,
                "RootDB": RootDB,
                "PackageVersion": PackageVersion,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Node"]) -> MetaOapg.properties.Node: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Arch"]) -> MetaOapg.properties.Arch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Platform"]) -> MetaOapg.properties.Platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Docker"]) -> MetaOapg.properties.Docker: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Database"]) -> MetaOapg.properties.Database: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProjectOnRootDB"]) -> MetaOapg.properties.ProjectOnRootDB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RootDB"]) -> MetaOapg.properties.RootDB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PackageVersion"]) -> MetaOapg.properties.PackageVersion: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Node", "Arch", "Platform", "Docker", "Database", "ProjectOnRootDB", "RootDB", "PackageVersion", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Node"]) -> typing.Union[MetaOapg.properties.Node, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Arch"]) -> typing.Union[MetaOapg.properties.Arch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Platform"]) -> typing.Union[MetaOapg.properties.Platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Docker"]) -> typing.Union[MetaOapg.properties.Docker, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Database"]) -> typing.Union[MetaOapg.properties.Database, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProjectOnRootDB"]) -> typing.Union[MetaOapg.properties.ProjectOnRootDB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RootDB"]) -> typing.Union[MetaOapg.properties.RootDB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PackageVersion"]) -> typing.Union[MetaOapg.properties.PackageVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Node", "Arch", "Platform", "Docker", "Database", "ProjectOnRootDB", "RootDB", "PackageVersion", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Node: typing.Union[MetaOapg.properties.Node, str, schemas.Unset] = schemas.unset,
        Arch: typing.Union[MetaOapg.properties.Arch, str, schemas.Unset] = schemas.unset,
        Platform: typing.Union[MetaOapg.properties.Platform, str, schemas.Unset] = schemas.unset,
        Docker: typing.Union[MetaOapg.properties.Docker, bool, schemas.Unset] = schemas.unset,
        Database: typing.Union[MetaOapg.properties.Database, str, schemas.Unset] = schemas.unset,
        ProjectOnRootDB: typing.Union[MetaOapg.properties.ProjectOnRootDB, bool, schemas.Unset] = schemas.unset,
        RootDB: typing.Union[MetaOapg.properties.RootDB, str, schemas.Unset] = schemas.unset,
        PackageVersion: typing.Union[MetaOapg.properties.PackageVersion, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BaseGetInfoByIdResponse':
        return super().__new__(
            cls,
            *args,
            Node=Node,
            Arch=Arch,
            Platform=Platform,
            Docker=Docker,
            Database=Database,
            ProjectOnRootDB=ProjectOnRootDB,
            RootDB=RootDB,
            PackageVersion=PackageVersion,
            _configuration=_configuration,
            **kwargs,
        )
