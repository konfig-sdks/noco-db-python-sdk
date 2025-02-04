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
from noco_db_python_sdk.type.public_list_nested_data_response_list import PublicListNestedDataResponseList

RequiredPublicListNestedDataResponse = TypedDict("RequiredPublicListNestedDataResponse", {
    "list": PublicListNestedDataResponseList,

    "pageInfo": Paginated,
    })

OptionalPublicListNestedDataResponse = TypedDict("OptionalPublicListNestedDataResponse", {
    }, total=False)

class PublicListNestedDataResponse(RequiredPublicListNestedDataResponse, OptionalPublicListNestedDataResponse):
    pass
