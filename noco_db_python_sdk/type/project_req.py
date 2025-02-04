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

from noco_db_python_sdk.type.base_req import BaseReq
from noco_db_python_sdk.type.meta import Meta
from noco_db_python_sdk.type.project_req_linked_db_project_ids import ProjectReqLinkedDbProjectIds
from noco_db_python_sdk.type.string_or_null import StringOrNull

class RequiredProjectReq(TypedDict):
    # Base Title
    title: str

class OptionalProjectReq(TypedDict, total=False):
    # Base Description
    description: str

    # Array of Bases
    sources: typing.List[BaseReq]

    # Primary Theme Color
    color: str

    status: StringOrNull

    type: str

    linked_db_project_ids: ProjectReqLinkedDbProjectIds

    meta: Meta

class ProjectReq(RequiredProjectReq, OptionalProjectReq):
    pass
