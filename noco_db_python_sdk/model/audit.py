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


class Audit(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Audit
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def id() -> typing.Type['Id']:
                return Id
            user = schemas.StrSchema
            display_name = schemas.StrSchema
            ip = schemas.StrSchema
            source_id = schemas.StrSchema
            base_id = schemas.StrSchema
            fk_model_id = schemas.StrSchema
            row_id = schemas.StrSchema
            
            
            class op_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "COMMENT": "COMMENT",
                        "DATA": "DATA",
                        "PROJECT": "PROJECT",
                        "VIRTUAL_RELATION": "VIRTUAL_RELATION",
                        "RELATION": "RELATION",
                        "TABLE_VIEW": "TABLE_VIEW",
                        "TABLE": "TABLE",
                        "VIEW": "VIEW",
                        "META": "META",
                        "WEBHOOKS": "WEBHOOKS",
                        "AUTHENTICATION": "AUTHENTICATION",
                        "TABLE_COLUMN": "TABLE_COLUMN",
                        "ORG_USER": "ORG_USER",
                    }
                
                @schemas.classproperty
                def COMMENT(cls):
                    return cls("COMMENT")
                
                @schemas.classproperty
                def DATA(cls):
                    return cls("DATA")
                
                @schemas.classproperty
                def PROJECT(cls):
                    return cls("PROJECT")
                
                @schemas.classproperty
                def VIRTUAL_RELATION(cls):
                    return cls("VIRTUAL_RELATION")
                
                @schemas.classproperty
                def RELATION(cls):
                    return cls("RELATION")
                
                @schemas.classproperty
                def TABLE_VIEW(cls):
                    return cls("TABLE_VIEW")
                
                @schemas.classproperty
                def TABLE(cls):
                    return cls("TABLE")
                
                @schemas.classproperty
                def VIEW(cls):
                    return cls("VIEW")
                
                @schemas.classproperty
                def META(cls):
                    return cls("META")
                
                @schemas.classproperty
                def WEBHOOKS(cls):
                    return cls("WEBHOOKS")
                
                @schemas.classproperty
                def AUTHENTICATION(cls):
                    return cls("AUTHENTICATION")
                
                @schemas.classproperty
                def TABLE_COLUMN(cls):
                    return cls("TABLE_COLUMN")
                
                @schemas.classproperty
                def ORG_USER(cls):
                    return cls("ORG_USER")
            
            
            class op_sub_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "UPDATE": "UPDATE",
                        "INSERT": "INSERT",
                        "BULK_INSERT": "BULK_INSERT",
                        "BULK_UPDATE": "BULK_UPDATE",
                        "BULK_DELETE": "BULK_DELETE",
                        "LINK_RECORD": "LINK_RECORD",
                        "UNLINK_RECORD": "UNLINK_RECORD",
                        "DELETE": "DELETE",
                        "CREATE": "CREATE",
                        "RENAME": "RENAME",
                        "IMPORT_FROM_ZIP": "IMPORT_FROM_ZIP",
                        "EXPORT_TO_FS": "EXPORT_TO_FS",
                        "EXPORT_TO_ZIP": "EXPORT_TO_ZIP",
                        "SIGNIN": "SIGNIN",
                        "SIGNUP": "SIGNUP",
                        "PASSWORD_RESET": "PASSWORD_RESET",
                        "PASSWORD_FORGOT": "PASSWORD_FORGOT",
                        "PASSWORD_CHANGE": "PASSWORD_CHANGE",
                        "EMAIL_VERIFICATION": "EMAIL_VERIFICATION",
                        "ROLES_MANAGEMENT": "ROLES_MANAGEMENT",
                        "INVITE": "INVITE",
                        "RESEND_INVITE": "RESEND_INVITE",
                    }
                
                @schemas.classproperty
                def UPDATE(cls):
                    return cls("UPDATE")
                
                @schemas.classproperty
                def INSERT(cls):
                    return cls("INSERT")
                
                @schemas.classproperty
                def BULK_INSERT(cls):
                    return cls("BULK_INSERT")
                
                @schemas.classproperty
                def BULK_UPDATE(cls):
                    return cls("BULK_UPDATE")
                
                @schemas.classproperty
                def BULK_DELETE(cls):
                    return cls("BULK_DELETE")
                
                @schemas.classproperty
                def LINK_RECORD(cls):
                    return cls("LINK_RECORD")
                
                @schemas.classproperty
                def UNLINK_RECORD(cls):
                    return cls("UNLINK_RECORD")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("DELETE")
                
                @schemas.classproperty
                def CREATE(cls):
                    return cls("CREATE")
                
                @schemas.classproperty
                def RENAME(cls):
                    return cls("RENAME")
                
                @schemas.classproperty
                def IMPORT_FROM_ZIP(cls):
                    return cls("IMPORT_FROM_ZIP")
                
                @schemas.classproperty
                def EXPORT_TO_FS(cls):
                    return cls("EXPORT_TO_FS")
                
                @schemas.classproperty
                def EXPORT_TO_ZIP(cls):
                    return cls("EXPORT_TO_ZIP")
                
                @schemas.classproperty
                def SIGNIN(cls):
                    return cls("SIGNIN")
                
                @schemas.classproperty
                def SIGNUP(cls):
                    return cls("SIGNUP")
                
                @schemas.classproperty
                def PASSWORD_RESET(cls):
                    return cls("PASSWORD_RESET")
                
                @schemas.classproperty
                def PASSWORD_FORGOT(cls):
                    return cls("PASSWORD_FORGOT")
                
                @schemas.classproperty
                def PASSWORD_CHANGE(cls):
                    return cls("PASSWORD_CHANGE")
                
                @schemas.classproperty
                def EMAIL_VERIFICATION(cls):
                    return cls("EMAIL_VERIFICATION")
                
                @schemas.classproperty
                def ROLES_MANAGEMENT(cls):
                    return cls("ROLES_MANAGEMENT")
                
                @schemas.classproperty
                def INVITE(cls):
                    return cls("INVITE")
                
                @schemas.classproperty
                def RESEND_INVITE(cls):
                    return cls("RESEND_INVITE")
            status = schemas.StrSchema
            details = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "id": id,
                "user": user,
                "display_name": display_name,
                "ip": ip,
                "source_id": source_id,
                "base_id": base_id,
                "fk_model_id": fk_model_id,
                "row_id": row_id,
                "op_type": op_type,
                "op_sub_type": op_sub_type,
                "status": status,
                "details": details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'Id': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip"]) -> MetaOapg.properties.ip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_id"]) -> MetaOapg.properties.source_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_id"]) -> MetaOapg.properties.base_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_model_id"]) -> MetaOapg.properties.fk_model_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["row_id"]) -> MetaOapg.properties.row_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op_type"]) -> MetaOapg.properties.op_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["op_sub_type"]) -> MetaOapg.properties.op_sub_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "user", "display_name", "ip", "source_id", "base_id", "fk_model_id", "row_id", "op_type", "op_sub_type", "status", "details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['Id', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip"]) -> typing.Union[MetaOapg.properties.ip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_id"]) -> typing.Union[MetaOapg.properties.source_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_id"]) -> typing.Union[MetaOapg.properties.base_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_model_id"]) -> typing.Union[MetaOapg.properties.fk_model_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["row_id"]) -> typing.Union[MetaOapg.properties.row_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["op_type"]) -> typing.Union[MetaOapg.properties.op_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["op_sub_type"]) -> typing.Union[MetaOapg.properties.op_sub_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "user", "display_name", "ip", "source_id", "base_id", "fk_model_id", "row_id", "op_type", "op_sub_type", "status", "details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union['Id', schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        ip: typing.Union[MetaOapg.properties.ip, str, schemas.Unset] = schemas.unset,
        source_id: typing.Union[MetaOapg.properties.source_id, str, schemas.Unset] = schemas.unset,
        base_id: typing.Union[MetaOapg.properties.base_id, str, schemas.Unset] = schemas.unset,
        fk_model_id: typing.Union[MetaOapg.properties.fk_model_id, str, schemas.Unset] = schemas.unset,
        row_id: typing.Union[MetaOapg.properties.row_id, str, schemas.Unset] = schemas.unset,
        op_type: typing.Union[MetaOapg.properties.op_type, str, schemas.Unset] = schemas.unset,
        op_sub_type: typing.Union[MetaOapg.properties.op_sub_type, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        details: typing.Union[MetaOapg.properties.details, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Audit':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            user=user,
            display_name=display_name,
            ip=ip,
            source_id=source_id,
            base_id=base_id,
            fk_model_id=fk_model_id,
            row_id=row_id,
            op_type=op_type,
            op_sub_type=op_sub_type,
            status=status,
            details=details,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.id import Id
