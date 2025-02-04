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

from noco_db_python_sdk.pydantic.grid_column import GridColumn
from noco_db_python_sdk.pydantic.id import Id
from noco_db_python_sdk.pydantic.meta import Meta

class Grid(BaseModel):
    id: typing.Optional[Id] = Field(None, alias='id')

    base_id: typing.Optional[Id] = Field(None, alias='base_id')

    source_id: typing.Optional[Id] = Field(None, alias='source_id')

    fk_view_id: typing.Optional[Id] = Field(None, alias='fk_view_id')

    # Row Height
    row_height: typing.Optional[typing.Union[int, float]] = Field(None, alias='row_height')

    meta: typing.Optional[Meta] = Field(None, alias='meta')

    # Grid View Columns
    columns: typing.Optional[typing.List[GridColumn]] = Field(None, alias='columns')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
