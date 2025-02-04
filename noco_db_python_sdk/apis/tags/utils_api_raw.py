# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_cache.delete import ClearNocoCacheRaw
from noco_db_python_sdk.paths.api_v2_meta_audits_comments_count.get import CountCommentsRaw
from noco_db_python_sdk.paths.api_v2_meta_audits_comments.post import CreateNewCommentRowRaw
from noco_db_python_sdk.paths.api_v2_meta_cache.get import GetAllNocoCacheRaw
from noco_db_python_sdk.paths.api_v2_meta_nocodb_info.get import GetAppInfoRaw
from noco_db_python_sdk.paths.api_v2_meta_audits_comments.get import ListCommentsRaw
from noco_db_python_sdk.paths.api_v2_meta_axios_request_make.post import MakeAxiosRequestRaw
from noco_db_python_sdk.paths.api_v2_meta_connection_select.post import SelectConnectionPostRaw
from noco_db_python_sdk.paths.api_v2_meta_connection_test.post import TestDbConnectionRaw
from noco_db_python_sdk.paths.api_v2_meta_audits_audit_id_comment.patch import UpdateAuditCommentRaw
from noco_db_python_sdk.paths.api_v2_meta_audits_rows_row_id_update.post import UpdateAuditRowRaw


class UtilsApiRaw(
    ClearNocoCacheRaw,
    CountCommentsRaw,
    CreateNewCommentRowRaw,
    GetAllNocoCacheRaw,
    GetAppInfoRaw,
    ListCommentsRaw,
    MakeAxiosRequestRaw,
    SelectConnectionPostRaw,
    TestDbConnectionRaw,
    UpdateAuditCommentRaw,
    UpdateAuditRowRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
