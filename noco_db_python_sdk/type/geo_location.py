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


class RequiredGeoLocation(TypedDict):
    pass

class OptionalGeoLocation(TypedDict, total=False):
    # The latitude of the location
    latitude: typing.Union[int, float]

    # The longitude of the location
    longitude: typing.Union[int, float]

class GeoLocation(RequiredGeoLocation, OptionalGeoLocation):
    pass