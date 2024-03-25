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


class BaseReq(BaseModel):
    # Source Name - Default BASE will be null by default
    alias: typing.Optional[str] = Field(None, alias='alias')

    # Source Configuration
    config: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='config')

    # Inflection for columns
    inflection_column: typing.Optional[str] = Field(None, alias='inflection_column')

    # Inflection for tables
    inflection_table: typing.Optional[str] = Field(None, alias='inflection_table')

    # Is the data source connected externally
    is_meta: typing.Optional[bool] = Field(None, alias='is_meta')

    # Is the data source minimal db
    is_local: typing.Optional[bool] = Field(None, alias='is_local')

    # DB Type
    type: typing.Optional[Literal["mssql", "mysql", "mysql2", "oracledb", "pg", "snowflake", "sqlite3"]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )