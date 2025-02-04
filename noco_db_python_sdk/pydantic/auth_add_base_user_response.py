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

from noco_db_python_sdk.pydantic.auth_add_base_user_response_error import AuthAddBaseUserResponseError

class AuthAddBaseUserResponse(BaseModel):
    # Success Message for inviting single email
    msg: typing.Optional[str] = Field(None, alias='msg')

    invite_token: typing.Optional[str] = Field(None, alias='invite_token')

    error: typing.Optional[AuthAddBaseUserResponseError] = Field(None, alias='error')

    email: typing.Optional[str] = Field(None, alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
