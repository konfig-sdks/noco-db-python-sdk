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

from noco_db_python_sdk.type.meta import Meta
from noco_db_python_sdk.type.normal_column_request import NormalColumnRequest

class RequiredTableReq(TypedDict):
    # The column models in this table
    columns: typing.List[NormalColumnRequest]

    # Table name
    table_name: str

class OptionalTableReq(TypedDict, total=False):
    # Table title
    title: str

    meta: Meta

    # The order of table list
    order: typing.Union[int, float]

class TableReq(RequiredTableReq, OptionalTableReq):
    pass
