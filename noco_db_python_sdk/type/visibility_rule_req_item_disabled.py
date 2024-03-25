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

from noco_db_python_sdk.type.model_bool import ModelBool

class RequiredVisibilityRuleReqItemDisabled(TypedDict):
    pass

class OptionalVisibilityRuleReqItemDisabled(TypedDict, total=False):
    commenter: ModelBool

    creator: ModelBool

    editor: ModelBool

    guest: ModelBool

    owner: ModelBool

    viewer: ModelBool

class VisibilityRuleReqItemDisabled(RequiredVisibilityRuleReqItemDisabled, OptionalVisibilityRuleReqItemDisabled):
    pass