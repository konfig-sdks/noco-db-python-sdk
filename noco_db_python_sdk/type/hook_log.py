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

from noco_db_python_sdk.type.model_bool import ModelBool
from noco_db_python_sdk.type.string_or_null import StringOrNull

class RequiredHookLog(TypedDict):
    pass

class OptionalHookLog(TypedDict, total=False):
    # Unique Source ID
    source_id: str

    # Hook Conditions
    conditions: str

    error: StringOrNull

    error_code: StringOrNull

    error_message: StringOrNull

    # Hook Event
    event: str

    # Execution Time in milliseconds
    execution_time: str

    fk_hook_id: StringOrNull

    id: StringOrNull

    # Hook Notification
    notifications: str

    # Hook Operation
    operation: str

    # Hook Payload
    payload: str

    # Base ID
    base_id: str

    response: StringOrNull

    test_call: ModelBool

    triggered_by: StringOrNull

    # Hook Type
    type: str

class HookLog(RequiredHookLog, OptionalHookLog):
    pass
