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


class User(BaseModel):
    # Unique identifier for the given user.
    id: str = Field(alias='id')

    email: str = Field(alias='email')

    # Set to true if the user's email has been verified.
    email_verified: bool = Field(alias='email_verified')

    roles: typing.Optional[str] = Field(None, alias='roles')

    # The date that the user was created.
    created_at: typing.Optional[date] = Field(None, alias='created_at')

    # The date that the user was created.
    updated_at: typing.Optional[date] = Field(None, alias='updated_at')

    display_name: typing.Optional[str] = Field(None, alias='display_name')

    user_name: typing.Optional[str] = Field(None, alias='user_name')

    bio: typing.Optional[str] = Field(None, alias='bio')

    location: typing.Optional[str] = Field(None, alias='location')

    website: typing.Optional[str] = Field(None, alias='website')

    avatar: typing.Optional[str] = Field(None, alias='avatar')

    # Access token version
    token_version: typing.Optional[str] = Field(None, alias='token_version')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )