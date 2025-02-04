# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_sorts_sort_id.delete import DeleteById
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_sorts.get import GetAllSorts
from noco_db_python_sdk.paths.api_v2_meta_sorts_sort_id.get import GetSortById
from noco_db_python_sdk.paths.api_v2_meta_sorts_sort_id.patch import UpdateSortById
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_sorts.post import UpdateViewSort
from noco_db_python_sdk.apis.tags.db_table_sort_api_raw import DBTableSortApiRaw


class DBTableSortApi(
    DeleteById,
    GetAllSorts,
    GetSortById,
    UpdateSortById,
    UpdateViewSort,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DBTableSortApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DBTableSortApiRaw(api_client)
