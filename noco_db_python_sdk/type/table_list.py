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

from noco_db_python_sdk.type.paginated import Paginated
from noco_db_python_sdk.type.table import Table

RequiredTableList = TypedDict("RequiredTableList", {
    # List of table objects
    "list": typing.List[Table],

    "pageInfo": Paginated,
    })

OptionalTableList = TypedDict("OptionalTableList", {
    }, total=False)

class TableList(RequiredTableList, OptionalTableList):
    pass