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


class TableRecordsReadByIdResponseJsonAddress(BaseModel):
    street: typing.Optional[str] = Field(None, alias='street')

    city: typing.Optional[str] = Field(None, alias='city')

    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )