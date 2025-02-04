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


class RequiredAuthAddBaseUserResponseErrorItem(TypedDict):
    pass

class OptionalAuthAddBaseUserResponseErrorItem(TypedDict, total=False):
    email: str

    error: str

class AuthAddBaseUserResponseErrorItem(RequiredAuthAddBaseUserResponseErrorItem, OptionalAuthAddBaseUserResponseErrorItem):
    pass
