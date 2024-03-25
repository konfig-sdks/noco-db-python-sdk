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

from noco_db_python_sdk.type.utils_test_db_connection_request_connection import UtilsTestDbConnectionRequestConnection

class RequiredUtilsTestDbConnectionRequest(TypedDict):
    pass

class OptionalUtilsTestDbConnectionRequest(TypedDict, total=False):
    # DB Type
    client: str

    connection: UtilsTestDbConnectionRequestConnection

class UtilsTestDbConnectionRequest(RequiredUtilsTestDbConnectionRequest, OptionalUtilsTestDbConnectionRequest):
    pass