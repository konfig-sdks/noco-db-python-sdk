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
from noco_db_python_sdk.type.table_records_list_response_list import TableRecordsListResponseList

RequiredTableRecordsListResponse = TypedDict("RequiredTableRecordsListResponse", {
    "list": TableRecordsListResponseList,

    "pageInfo": Paginated,
    })

OptionalTableRecordsListResponse = TypedDict("OptionalTableRecordsListResponse", {
    }, total=False)

class TableRecordsListResponse(RequiredTableRecordsListResponse, OptionalTableRecordsListResponse):
    pass