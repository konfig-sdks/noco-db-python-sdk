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


class TableRecordsReadByIdResponseJsonScores(BaseModel):
    math: typing.Optional[typing.Union[int, float]] = Field(None, alias='math')

    science: typing.Optional[typing.Union[int, float]] = Field(None, alias='science')

    history: typing.Optional[typing.Union[int, float]] = Field(None, alias='history')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
