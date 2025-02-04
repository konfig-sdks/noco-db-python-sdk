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
from noco_db_python_sdk.type.string_or_null import StringOrNull

class RequiredPlugin(TypedDict):
    pass

class OptionalPlugin(TypedDict, total=False):
    # Plugin tags
    tags: str

    # Plugin Title
    title: str

    # Plugin Description
    description: str

    # Plugin Version
    version: str

    active: ModelBool

    # Plugin Category
    category: str

    # Plugin Creator (Not in use)
    creator: str

    # Plugin Creator website (Not in use)
    creator_website: str

    # Documentation of plugin (Not in use)
    docs: str

    # Plugin Icon (Not in use)
    icon: str

    id: Id

    # Plugin Input
    input: typing.Union[StringOrNull, int]

    # Plugin Input Schema 
    input_schema: str

    # Plugin logo
    logo: str

    # Plugin Price (Not in use)
    price: str

    # Plugin Rating (Not in use)
    rating: typing.Union[int, float]

    # Plugin Status
    status: str

    # Not in use
    status_details: str

class Plugin(RequiredPlugin, OptionalPlugin):
    pass
