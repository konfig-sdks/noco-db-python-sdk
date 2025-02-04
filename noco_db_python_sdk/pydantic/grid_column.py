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

from noco_db_python_sdk.pydantic.id import Id
from noco_db_python_sdk.pydantic.model_bool import ModelBool
from noco_db_python_sdk.pydantic.string_or_null import StringOrNull

class GridColumn(BaseModel):
    id: typing.Optional[Id] = Field(None, alias='id')

    fk_view_id: typing.Optional[Id] = Field(None, alias='fk_view_id')

    fk_column_id: typing.Optional[Id] = Field(None, alias='fk_column_id')

    base_id: typing.Optional[Id] = Field(None, alias='base_id')

    source_id: typing.Optional[Id] = Field(None, alias='source_id')

    show: typing.Optional[ModelBool] = Field(None, alias='show')

    # Grid Column Order
    order: typing.Optional[typing.Union[int, float]] = Field(None, alias='order')

    # Column Width
    width: typing.Optional[str] = Field(None, alias='width')

    help: typing.Optional[StringOrNull] = Field(None, alias='help')

    group_by: typing.Optional[ModelBool] = Field(None, alias='group_by')

    # Group By Order
    group_by_order: typing.Optional[typing.Union[int, float]] = Field(None, alias='group_by_order')

    group_by_sort: typing.Optional[StringOrNull] = Field(None, alias='group_by_sort')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
