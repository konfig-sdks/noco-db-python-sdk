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


class TableRecordsReadByIdResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            Id = schemas.NumberSchema
            SingleLineText = schemas.StrSchema
            CreatedAt = schemas.StrSchema
            UpdatedAt = schemas.StrSchema
            Year = schemas.NumberSchema
            URL = schemas.StrSchema
            SingleSelect = schemas.StrSchema
            Email = schemas.StrSchema
            Duration = schemas.NumberSchema
            Decimal = schemas.NumberSchema
            Currency = schemas.NumberSchema
            Barcode = schemas.StrSchema
        
            @staticmethod
            def JSON() -> typing.Type['TableRecordsReadByIdResponseJson']:
                return TableRecordsReadByIdResponseJson
            QRCode = schemas.StrSchema
            Rollup = schemas.NumberSchema
            Date = schemas.StrSchema
            Time = schemas.StrSchema
            Rating = schemas.NumberSchema
            Percent = schemas.NumberSchema
            Formula = schemas.NumberSchema
            Checkbox = schemas.BoolSchema
        
            @staticmethod
            def Attachment() -> typing.Type['TableRecordsReadByIdResponseAttachment']:
                return TableRecordsReadByIdResponseAttachment
            MultiSelect = schemas.StrSchema
            DateTime = schemas.StrSchema
            LongText = schemas.StrSchema
            Geometry = schemas.StrSchema
            PhoneNumber = schemas.StrSchema
            Number = schemas.NumberSchema
            linkshas_many = schemas.NumberSchema
            linksmany_many = schemas.NumberSchema
        
            @staticmethod
            def linksbelongs_to() -> typing.Type['TableRecordsReadByIdResponseLinksbelongsTo']:
                return TableRecordsReadByIdResponseLinksbelongsTo
            Lookup = schemas.StrSchema
            __annotations__ = {
                "Id": Id,
                "SingleLineText": SingleLineText,
                "CreatedAt": CreatedAt,
                "UpdatedAt": UpdatedAt,
                "Year": Year,
                "URL": URL,
                "SingleSelect": SingleSelect,
                "Email": Email,
                "Duration": Duration,
                "Decimal": Decimal,
                "Currency": Currency,
                "Barcode": Barcode,
                "JSON": JSON,
                "QRCode": QRCode,
                "Rollup": Rollup,
                "Date": Date,
                "Time": Time,
                "Rating": Rating,
                "Percent": Percent,
                "Formula": Formula,
                "Checkbox": Checkbox,
                "Attachment": Attachment,
                "MultiSelect": MultiSelect,
                "DateTime": DateTime,
                "LongText": LongText,
                "Geometry": Geometry,
                "PhoneNumber": PhoneNumber,
                "Number": Number,
                "Links:has-many": linkshas_many,
                "Links:many-many": linksmany_many,
                "Links:belongs-to": linksbelongs_to,
                "Lookup": Lookup,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Id"]) -> MetaOapg.properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SingleLineText"]) -> MetaOapg.properties.SingleLineText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CreatedAt"]) -> MetaOapg.properties.CreatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UpdatedAt"]) -> MetaOapg.properties.UpdatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Year"]) -> MetaOapg.properties.Year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["URL"]) -> MetaOapg.properties.URL: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SingleSelect"]) -> MetaOapg.properties.SingleSelect: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Duration"]) -> MetaOapg.properties.Duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Decimal"]) -> MetaOapg.properties.Decimal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Currency"]) -> MetaOapg.properties.Currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Barcode"]) -> MetaOapg.properties.Barcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["JSON"]) -> 'TableRecordsReadByIdResponseJson': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["QRCode"]) -> MetaOapg.properties.QRCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rollup"]) -> MetaOapg.properties.Rollup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Date"]) -> MetaOapg.properties.Date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Time"]) -> MetaOapg.properties.Time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rating"]) -> MetaOapg.properties.Rating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Percent"]) -> MetaOapg.properties.Percent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Formula"]) -> MetaOapg.properties.Formula: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Checkbox"]) -> MetaOapg.properties.Checkbox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Attachment"]) -> 'TableRecordsReadByIdResponseAttachment': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MultiSelect"]) -> MetaOapg.properties.MultiSelect: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DateTime"]) -> MetaOapg.properties.DateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LongText"]) -> MetaOapg.properties.LongText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Geometry"]) -> MetaOapg.properties.Geometry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PhoneNumber"]) -> MetaOapg.properties.PhoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Number"]) -> MetaOapg.properties.Number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links:has-many"]) -> MetaOapg.properties.linkshas_many: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links:many-many"]) -> MetaOapg.properties.linksmany_many: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Links:belongs-to"]) -> 'TableRecordsReadByIdResponseLinksbelongsTo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Lookup"]) -> MetaOapg.properties.Lookup: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Id", "SingleLineText", "CreatedAt", "UpdatedAt", "Year", "URL", "SingleSelect", "Email", "Duration", "Decimal", "Currency", "Barcode", "JSON", "QRCode", "Rollup", "Date", "Time", "Rating", "Percent", "Formula", "Checkbox", "Attachment", "MultiSelect", "DateTime", "LongText", "Geometry", "PhoneNumber", "Number", "Links:has-many", "Links:many-many", "Links:belongs-to", "Lookup", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Id"]) -> typing.Union[MetaOapg.properties.Id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SingleLineText"]) -> typing.Union[MetaOapg.properties.SingleLineText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CreatedAt"]) -> typing.Union[MetaOapg.properties.CreatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UpdatedAt"]) -> typing.Union[MetaOapg.properties.UpdatedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Year"]) -> typing.Union[MetaOapg.properties.Year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["URL"]) -> typing.Union[MetaOapg.properties.URL, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SingleSelect"]) -> typing.Union[MetaOapg.properties.SingleSelect, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Duration"]) -> typing.Union[MetaOapg.properties.Duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Decimal"]) -> typing.Union[MetaOapg.properties.Decimal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Currency"]) -> typing.Union[MetaOapg.properties.Currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Barcode"]) -> typing.Union[MetaOapg.properties.Barcode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["JSON"]) -> typing.Union['TableRecordsReadByIdResponseJson', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["QRCode"]) -> typing.Union[MetaOapg.properties.QRCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rollup"]) -> typing.Union[MetaOapg.properties.Rollup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Date"]) -> typing.Union[MetaOapg.properties.Date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Time"]) -> typing.Union[MetaOapg.properties.Time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Rating"]) -> typing.Union[MetaOapg.properties.Rating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Percent"]) -> typing.Union[MetaOapg.properties.Percent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Formula"]) -> typing.Union[MetaOapg.properties.Formula, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Checkbox"]) -> typing.Union[MetaOapg.properties.Checkbox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Attachment"]) -> typing.Union['TableRecordsReadByIdResponseAttachment', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MultiSelect"]) -> typing.Union[MetaOapg.properties.MultiSelect, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DateTime"]) -> typing.Union[MetaOapg.properties.DateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LongText"]) -> typing.Union[MetaOapg.properties.LongText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Geometry"]) -> typing.Union[MetaOapg.properties.Geometry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PhoneNumber"]) -> typing.Union[MetaOapg.properties.PhoneNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Number"]) -> typing.Union[MetaOapg.properties.Number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links:has-many"]) -> typing.Union[MetaOapg.properties.linkshas_many, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links:many-many"]) -> typing.Union[MetaOapg.properties.linksmany_many, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Links:belongs-to"]) -> typing.Union['TableRecordsReadByIdResponseLinksbelongsTo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Lookup"]) -> typing.Union[MetaOapg.properties.Lookup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Id", "SingleLineText", "CreatedAt", "UpdatedAt", "Year", "URL", "SingleSelect", "Email", "Duration", "Decimal", "Currency", "Barcode", "JSON", "QRCode", "Rollup", "Date", "Time", "Rating", "Percent", "Formula", "Checkbox", "Attachment", "MultiSelect", "DateTime", "LongText", "Geometry", "PhoneNumber", "Number", "Links:has-many", "Links:many-many", "Links:belongs-to", "Lookup", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        Id: typing.Union[MetaOapg.properties.Id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        SingleLineText: typing.Union[MetaOapg.properties.SingleLineText, str, schemas.Unset] = schemas.unset,
        CreatedAt: typing.Union[MetaOapg.properties.CreatedAt, str, schemas.Unset] = schemas.unset,
        UpdatedAt: typing.Union[MetaOapg.properties.UpdatedAt, str, schemas.Unset] = schemas.unset,
        Year: typing.Union[MetaOapg.properties.Year, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        URL: typing.Union[MetaOapg.properties.URL, str, schemas.Unset] = schemas.unset,
        SingleSelect: typing.Union[MetaOapg.properties.SingleSelect, str, schemas.Unset] = schemas.unset,
        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
        Duration: typing.Union[MetaOapg.properties.Duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Decimal: typing.Union[MetaOapg.properties.Decimal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Currency: typing.Union[MetaOapg.properties.Currency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Barcode: typing.Union[MetaOapg.properties.Barcode, str, schemas.Unset] = schemas.unset,
        JSON: typing.Union['TableRecordsReadByIdResponseJson', schemas.Unset] = schemas.unset,
        QRCode: typing.Union[MetaOapg.properties.QRCode, str, schemas.Unset] = schemas.unset,
        Rollup: typing.Union[MetaOapg.properties.Rollup, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Date: typing.Union[MetaOapg.properties.Date, str, schemas.Unset] = schemas.unset,
        Time: typing.Union[MetaOapg.properties.Time, str, schemas.Unset] = schemas.unset,
        Rating: typing.Union[MetaOapg.properties.Rating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Percent: typing.Union[MetaOapg.properties.Percent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Formula: typing.Union[MetaOapg.properties.Formula, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Checkbox: typing.Union[MetaOapg.properties.Checkbox, bool, schemas.Unset] = schemas.unset,
        Attachment: typing.Union['TableRecordsReadByIdResponseAttachment', schemas.Unset] = schemas.unset,
        MultiSelect: typing.Union[MetaOapg.properties.MultiSelect, str, schemas.Unset] = schemas.unset,
        DateTime: typing.Union[MetaOapg.properties.DateTime, str, schemas.Unset] = schemas.unset,
        LongText: typing.Union[MetaOapg.properties.LongText, str, schemas.Unset] = schemas.unset,
        Geometry: typing.Union[MetaOapg.properties.Geometry, str, schemas.Unset] = schemas.unset,
        PhoneNumber: typing.Union[MetaOapg.properties.PhoneNumber, str, schemas.Unset] = schemas.unset,
        Number: typing.Union[MetaOapg.properties.Number, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Lookup: typing.Union[MetaOapg.properties.Lookup, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TableRecordsReadByIdResponse':
        return super().__new__(
            cls,
            *args,
            Id=Id,
            SingleLineText=SingleLineText,
            CreatedAt=CreatedAt,
            UpdatedAt=UpdatedAt,
            Year=Year,
            URL=URL,
            SingleSelect=SingleSelect,
            Email=Email,
            Duration=Duration,
            Decimal=Decimal,
            Currency=Currency,
            Barcode=Barcode,
            JSON=JSON,
            QRCode=QRCode,
            Rollup=Rollup,
            Date=Date,
            Time=Time,
            Rating=Rating,
            Percent=Percent,
            Formula=Formula,
            Checkbox=Checkbox,
            Attachment=Attachment,
            MultiSelect=MultiSelect,
            DateTime=DateTime,
            LongText=LongText,
            Geometry=Geometry,
            PhoneNumber=PhoneNumber,
            Number=Number,
            Lookup=Lookup,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.table_records_read_by_id_response_attachment import TableRecordsReadByIdResponseAttachment
from noco_db_python_sdk.model.table_records_read_by_id_response_json import TableRecordsReadByIdResponseJson
from noco_db_python_sdk.model.table_records_read_by_id_response_linksbelongs_to import TableRecordsReadByIdResponseLinksbelongsTo