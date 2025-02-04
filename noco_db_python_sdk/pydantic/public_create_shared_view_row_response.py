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


class PublicCreateSharedViewRowResponse(BaseModel):
    id: typing.Optional[typing.Union[int, float]] = Field(None, alias='Id')

    col1: typing.Optional[str] = Field(None, alias='col1')

    col2: typing.Optional[str] = Field(None, alias='col2')

    created_at: typing.Optional[str] = Field(None, alias='CreatedAt')

    updated_at: typing.Optional[str] = Field(None, alias='UpdatedAt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
