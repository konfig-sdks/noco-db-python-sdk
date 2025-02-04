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

from noco_db_python_sdk.type.formula import Formula
from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.link_to_another_record import LinkToAnotherRecord
from noco_db_python_sdk.type.lookup import Lookup
from noco_db_python_sdk.type.meta import Meta
from noco_db_python_sdk.type.model_bool import ModelBool
from noco_db_python_sdk.type.rollup import Rollup
from noco_db_python_sdk.type.select_options import SelectOptions
from noco_db_python_sdk.type.string_or_null import StringOrNull
from noco_db_python_sdk.type.string_or_null_or_boolean_or_number import StringOrNullOrBooleanOrNumber

class RequiredColumn(TypedDict):
    pass

class OptionalColumn(TypedDict, total=False):
    # Column Title
    title: str

    ai: ModelBool

    au: ModelBool

    # Source ID that this column belongs to
    source_id: str

    # Column Comment
    cc: str

    cdf: StringOrNullOrBooleanOrNumber

    # Character Maximum Length
    clen: typing.Union[int, none_type, str]

    # Column Options
    colOptions: typing.Union[Formula, LinkToAnotherRecord, Lookup, Rollup, SelectOptions, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # Column Name
    column_name: str

    # Column Ordinal Position
    cop: str

    csn: StringOrNull

    # Column Type
    ct: str

    deleted: ModelBool

    # Data Type in DB
    dt: str

    # Data Type X
    dtx: str

    # Data Type X Precision
    dtxp: typing.Union[none_type, typing.Union[int, float], str]

    # Data Type X Scale
    dtxs: typing.Union[none_type, typing.Union[int, float], str]

    # Model ID that this column belongs to
    fk_model_id: str

    id: Id

    meta: Meta

    # Numeric Precision
    np: typing.Union[int, none_type, str]

    # Numeric Scale
    ns: typing.Union[int, none_type, str]

    # The order of the list of columns
    order: typing.Union[int, float]

    pk: ModelBool

    pv: ModelBool

    rqd: ModelBool

    system: ModelBool

    # The data type in UI
    uidt: str

    un: ModelBool

    unique: ModelBool

    visible: ModelBool

class Column(RequiredColumn, OptionalColumn):
    pass
