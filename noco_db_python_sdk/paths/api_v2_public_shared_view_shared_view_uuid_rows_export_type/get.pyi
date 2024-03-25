# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from noco_db_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from noco_db_python_sdk.api_response import AsyncGeneratorResponse
from noco_db_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from noco_db_python_sdk import schemas  # noqa: F401

from noco_db_python_sdk.model.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponseSchema

from noco_db_python_sdk.type.auth_list_base_users400_response import AuthListBaseUsers400Response

from ...api_client import Dictionary
from noco_db_python_sdk.pydantic.auth_list_base_users400_response import AuthListBaseUsers400Response as AuthListBaseUsers400ResponsePydantic

# Path params
SharedViewUuidSchema = schemas.StrSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
    
    @schemas.classproperty
    def EXCEL(cls):
        return cls("excel")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'sharedViewUuid': typing.Union[SharedViewUuidSchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_shared_view_uuid = api_client.PathParameter(
    name="sharedViewUuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=SharedViewUuidSchema,
    required=True,
)
request_path_type = api_client.PathParameter(
    name="type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TypeSchema,
    required=True,
)
NcExportOffsetSchema = schemas.IntSchema
SchemaFor200ResponseBodyApplicationOctetStream = schemas.AnyTypeSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'nc-export-offset': NcExportOffsetSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Union[bool, date, datetime, dict, float, int, list, str, None]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Union[bool, date, datetime, dict, float, int, list, str, None]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/octet-stream': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationOctetStream),
    },
    headers=[
        nc_export_offset_parameter,
    ]
)
SchemaFor400ResponseBodyApplicationJson = AuthListBaseUsers400ResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: AuthListBaseUsers400Response


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: AuthListBaseUsers400Response


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/octet-stream',
    'application/json',
)


class BaseApi(api_client.Api):

    def _rows_export_type_mapped_args(
        self,
        shared_view_uuid: str,
        type: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if shared_view_uuid is not None:
            _path_params["sharedViewUuid"] = shared_view_uuid
        if type is not None:
            _path_params["type"] = type
        args.path = _path_params
        return args

    async def _arows_export_type_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Export Rows in Share View
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_shared_view_uuid,
            request_path_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/public/shared-view/{sharedViewUuid}/rows/export/{type}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _rows_export_type_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Export Rows in Share View
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_shared_view_uuid,
            request_path_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/public/shared-view/{sharedViewUuid}/rows/export/{type}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RowsExportTypeRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arows_export_type(
        self,
        shared_view_uuid: str,
        type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._rows_export_type_mapped_args(
            shared_view_uuid=shared_view_uuid,
            type=type,
        )
        return await self._arows_export_type_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def rows_export_type(
        self,
        shared_view_uuid: str,
        type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._rows_export_type_mapped_args(
            shared_view_uuid=shared_view_uuid,
            type=type,
        )
        return self._rows_export_type_oapg(
            path_params=args.path,
        )

class RowsExportType(BaseApi):

    async def arows_export_type(
        self,
        shared_view_uuid: str,
        type: str,
        validate: bool = False,
        **kwargs,
    ) -> typing.Union[bool, date, datetime, dict, float, int, list, str, None]:
        raw_response = await self.raw.arows_export_type(
            shared_view_uuid=shared_view_uuid,
            type=type,
            **kwargs,
        )
        if validate:
            return RootModel[typing.Union[bool, date, datetime, dict, float, int, list, str, None]](raw_response.body).root
        return raw_response.body
    
    
    def rows_export_type(
        self,
        shared_view_uuid: str,
        type: str,
        validate: bool = False,
    ) -> typing.Union[bool, date, datetime, dict, float, int, list, str, None]:
        raw_response = self.raw.rows_export_type(
            shared_view_uuid=shared_view_uuid,
            type=type,
        )
        if validate:
            return RootModel[typing.Union[bool, date, datetime, dict, float, int, list, str, None]](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        shared_view_uuid: str,
        type: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._rows_export_type_mapped_args(
            shared_view_uuid=shared_view_uuid,
            type=type,
        )
        return await self._arows_export_type_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        shared_view_uuid: str,
        type: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._rows_export_type_mapped_args(
            shared_view_uuid=shared_view_uuid,
            type=type,
        )
        return self._rows_export_type_oapg(
            path_params=args.path,
        )
