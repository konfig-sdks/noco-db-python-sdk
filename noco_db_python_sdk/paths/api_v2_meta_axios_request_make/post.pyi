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

# Header params
XcAuthSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'xc-auth': typing.Union[XcAuthSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_xc_auth = api_client.HeaderParameter(
    name="xc-auth",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XcAuthSchema,
)
# body param
SchemaForRequestBodyApplicationJson = schemas.DictSchema


request_body_body = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
    'application/json',
)


class BaseApi(api_client.Api):

    def _make_axios_request_mapped_args(
        self,
        xc_auth: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        args.body = _body
        if xc_auth is not None:
            _header_params["xc-auth"] = xc_auth
        args.header = _header_params
        return args

    async def _amake_axios_request_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Axios Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xc_auth,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/axiosRequestMake',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _make_axios_request_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Axios Request
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_xc_auth,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/meta/axiosRequestMake',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_body.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class MakeAxiosRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def amake_axios_request(
        self,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._make_axios_request_mapped_args(
            xc_auth=xc_auth,
        )
        return await self._amake_axios_request_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def make_axios_request(
        self,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._make_axios_request_mapped_args(
            xc_auth=xc_auth,
        )
        return self._make_axios_request_oapg(
            body=args.body,
            header_params=args.header,
        )

class MakeAxiosRequest(BaseApi):

    async def amake_axios_request(
        self,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.amake_axios_request(
            xc_auth=xc_auth,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def make_axios_request(
        self,
        xc_auth: typing.Optional[str] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.make_axios_request(
            xc_auth=xc_auth,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        xc_auth: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._make_axios_request_mapped_args(
            xc_auth=xc_auth,
        )
        return await self._amake_axios_request_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        xc_auth: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._make_axios_request_mapped_args(
            xc_auth=xc_auth,
        )
        return self._make_axios_request_oapg(
            body=args.body,
            header_params=args.header,
        )

