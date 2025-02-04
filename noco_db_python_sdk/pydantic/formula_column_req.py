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


class FormulaColumnReq(BaseModel):
    # Formula Title
    title: typing.Optional[str] = Field(None, alias='title')

    # Formula with column ID replaced
    formula: typing.Optional[str] = Field(None, alias='formula')

    # Original Formula inputted in UI
    formula_raw: typing.Optional[str] = Field(None, alias='formula_raw')

    # UI Data Type
    uidt: typing.Optional[Literal["Formula"]] = Field(None, alias='uidt')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
