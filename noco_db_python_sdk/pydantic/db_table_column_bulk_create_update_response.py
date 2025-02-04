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

from noco_db_python_sdk.pydantic.db_table_column_bulk_create_update_response_failed_ops import DbTableColumnBulkCreateUpdateResponseFailedOps

class DbTableColumnBulkCreateUpdateResponse(BaseModel):
    failed_ops: typing.Optional[DbTableColumnBulkCreateUpdateResponseFailedOps] = Field(None, alias='failedOps')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
