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

from noco_db_python_sdk.type.auth_add_base_user_response_error import AuthAddBaseUserResponseError

class RequiredAuthAddBaseUserResponse(TypedDict):
    pass

class OptionalAuthAddBaseUserResponse(TypedDict, total=False):
    # Success Message for inviting single email
    msg: str

    invite_token: str

    error: AuthAddBaseUserResponseError

    email: str

class AuthAddBaseUserResponse(RequiredAuthAddBaseUserResponse, OptionalAuthAddBaseUserResponse):
    pass
