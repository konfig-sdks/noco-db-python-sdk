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


class SortEvent(BaseModel):
    # The ID of the user who created sort
    fk_user_id: str = Field(alias='fk_user_id')

    type: str = Field(alias='type')

    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='body')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )