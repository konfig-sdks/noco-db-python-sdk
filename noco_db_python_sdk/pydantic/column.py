# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from noco_db_python_sdk.pydantic.formula import Formula
from noco_db_python_sdk.pydantic.id import Id
from noco_db_python_sdk.pydantic.link_to_another_record import LinkToAnotherRecord
from noco_db_python_sdk.pydantic.lookup import Lookup
from noco_db_python_sdk.pydantic.meta import Meta
from noco_db_python_sdk.pydantic.model_bool import ModelBool
from noco_db_python_sdk.pydantic.rollup import Rollup
from noco_db_python_sdk.pydantic.select_options import SelectOptions
from noco_db_python_sdk.pydantic.string_or_null import StringOrNull
from noco_db_python_sdk.pydantic.string_or_null_or_boolean_or_number import StringOrNullOrBooleanOrNumber

class Column(BaseModel):
    # Column Title
    title: typing.Optional[str] = Field(None, alias='title')

    ai: typing.Optional[ModelBool] = Field(None, alias='ai')

    au: typing.Optional[ModelBool] = Field(None, alias='au')

    # Source ID that this column belongs to
    source_id: typing.Optional[str] = Field(None, alias='source_id')

    # Column Comment
    cc: typing.Optional[str] = Field(None, alias='cc')

    cdf: typing.Optional[StringOrNullOrBooleanOrNumber] = Field(None, alias='cdf')

    # Character Maximum Length
    clen: typing.Optional[typing.Union[int, none_type, str]] = Field(None, alias='clen')

    # Column Options
    col_options: typing.Optional[typing.Union[Formula, LinkToAnotherRecord, Lookup, Rollup, SelectOptions, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='colOptions')

    # Column Name
    column_name: typing.Optional[str] = Field(None, alias='column_name')

    # Column Ordinal Position
    cop: typing.Optional[str] = Field(None, alias='cop')

    csn: typing.Optional[StringOrNull] = Field(None, alias='csn')

    # Column Type
    ct: typing.Optional[str] = Field(None, alias='ct')

    deleted: typing.Optional[ModelBool] = Field(None, alias='deleted')

    # Data Type in DB
    dt: typing.Optional[str] = Field(None, alias='dt')

    # Data Type X
    dtx: typing.Optional[str] = Field(None, alias='dtx')

    # Data Type X Precision
    dtxp: typing.Optional[typing.Union[none_type, typing.Union[int, float], str]] = Field(None, alias='dtxp')

    # Data Type X Scale
    dtxs: typing.Optional[typing.Union[none_type, typing.Union[int, float], str]] = Field(None, alias='dtxs')

    # Model ID that this column belongs to
    fk_model_id: typing.Optional[str] = Field(None, alias='fk_model_id')

    id: typing.Optional[Id] = Field(None, alias='id')

    meta: typing.Optional[Meta] = Field(None, alias='meta')

    # Numeric Precision
    np: typing.Optional[typing.Union[int, none_type, str]] = Field(None, alias='np')

    # Numeric Scale
    ns: typing.Optional[typing.Union[int, none_type, str]] = Field(None, alias='ns')

    # The order of the list of columns
    order: typing.Optional[typing.Union[int, float]] = Field(None, alias='order')

    pk: typing.Optional[ModelBool] = Field(None, alias='pk')

    pv: typing.Optional[ModelBool] = Field(None, alias='pv')

    rqd: typing.Optional[ModelBool] = Field(None, alias='rqd')

    system: typing.Optional[ModelBool] = Field(None, alias='system')

    # The data type in UI
    uidt: typing.Optional[Literal["Attachment", "AutoNumber", "Barcode", "Button", "Checkbox", "Collaborator", "Count", "CreatedTime", "Currency", "Date", "DateTime", "Decimal", "Duration", "Email", "Formula", "ForeignKey", "GeoData", "Geometry", "ID", "JSON", "LastModifiedTime", "LongText", "LinkToAnotherRecord", "Lookup", "MultiSelect", "Number", "Percent", "PhoneNumber", "Rating", "Rollup", "SingleLineText", "SingleSelect", "SpecificDBType", "Time", "URL", "Year", "QrCode", "Links", "User", "CreatedBy", "LastModifiedBy"]] = Field(None, alias='uidt')

    un: typing.Optional[ModelBool] = Field(None, alias='un')

    unique: typing.Optional[ModelBool] = Field(None, alias='unique')

    visible: typing.Optional[ModelBool] = Field(None, alias='visible')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
