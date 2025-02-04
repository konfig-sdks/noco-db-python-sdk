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

from noco_db_python_sdk.type.hook_log import HookLog
from noco_db_python_sdk.type.paginated import Paginated

RequiredHookLogList = TypedDict("RequiredHookLogList", {
    # List of hook objects
    "list": typing.List[HookLog],

    "pageInfo": Paginated,
    })

OptionalHookLogList = TypedDict("OptionalHookLogList", {
    }, total=False)

class HookLogList(RequiredHookLogList, OptionalHookLogList):
    pass
