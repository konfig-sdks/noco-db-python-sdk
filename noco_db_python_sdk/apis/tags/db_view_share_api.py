# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.post import CreateSharedView
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.delete import DeleteSharedView
from noco_db_python_sdk.paths.api_v2_meta_tables_table_id_share.get import ListSharedViews
from noco_db_python_sdk.paths.api_v2_meta_views_view_id_share.patch import UpdateSharedView
from noco_db_python_sdk.apis.tags.db_view_share_api_raw import DBViewShareApiRaw


class DBViewShareApi(
    CreateSharedView,
    DeleteSharedView,
    ListSharedViews,
    UpdateSharedView,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DBViewShareApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DBViewShareApiRaw(api_client)