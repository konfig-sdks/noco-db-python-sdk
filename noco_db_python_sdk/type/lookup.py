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

class RequiredLookup(TypedDict):
    pass

class OptionalLookup(TypedDict, total=False):
    id: Id

    fk_column_id: Id

    fk_lookup_column_id: Id

    fk_relation_column_id: Id

    # The order among the list
    order: typing.Union[int, float]

class Lookup(RequiredLookup, OptionalLookup):
    pass
