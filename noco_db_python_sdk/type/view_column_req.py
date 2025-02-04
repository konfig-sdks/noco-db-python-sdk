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

from noco_db_python_sdk.type.id import Id
from noco_db_python_sdk.type.model_bool import ModelBool

class RequiredViewColumnReq(TypedDict):
    pass

class OptionalViewColumnReq(TypedDict, total=False):
    fk_column_id: Id

    show: ModelBool

    # The order of the list of views.
    order: typing.Union[int, float]

class ViewColumnReq(RequiredViewColumnReq, OptionalViewColumnReq):
    pass
