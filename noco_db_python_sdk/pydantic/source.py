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

from noco_db_python_sdk.pydantic.model_bool import ModelBool
from noco_db_python_sdk.pydantic.string_or_null import StringOrNull

class Source(BaseModel):
    alias: typing.Optional[StringOrNull] = Field(None, alias='alias')

    # Source Configuration
    config: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='config')

    enabled: typing.Optional[ModelBool] = Field(None, alias='enabled')

    # Unique Source ID
    id: typing.Optional[str] = Field(None, alias='id')

    # Inflection for columns
    inflection_column: typing.Optional[str] = Field(None, alias='inflection_column')

    # Inflection for tables
    inflection_table: typing.Optional[str] = Field(None, alias='inflection_table')

    is_meta: typing.Optional[ModelBool] = Field(None, alias='is_meta')

    is_local: typing.Optional[ModelBool] = Field(None, alias='is_local')

    # The order of the list of sources
    order: typing.Optional[typing.Union[int, float]] = Field(None, alias='order')

    # The base ID that this source belongs to
    base_id: typing.Optional[str] = Field(None, alias='base_id')

    # DB Type
    type: typing.Optional[Literal["mssql", "mysql", "mysql2", "oracledb", "pg", "snowflake", "sqlite3"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )