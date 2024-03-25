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


class RequiredPublicCreateSharedViewRowResponse(TypedDict):
    pass

class OptionalPublicCreateSharedViewRowResponse(TypedDict, total=False):
    Id: typing.Union[int, float]

    col1: str

    col2: str

    CreatedAt: str

    UpdatedAt: str

class PublicCreateSharedViewRowResponse(RequiredPublicCreateSharedViewRowResponse, OptionalPublicCreateSharedViewRowResponse):
    pass