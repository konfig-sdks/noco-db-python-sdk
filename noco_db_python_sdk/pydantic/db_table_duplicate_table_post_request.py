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

from noco_db_python_sdk.pydantic.db_table_duplicate_table_post_request_options import DbTableDuplicateTablePostRequestOptions

class DbTableDuplicateTablePostRequest(BaseModel):
    options: typing.Optional[DbTableDuplicateTablePostRequestOptions] = Field(None, alias='options')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
