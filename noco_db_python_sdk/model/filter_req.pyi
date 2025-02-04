# coding: utf-8

"""
    NocoDB v2

    NocoDB API Documentation

    Generated by: https://konfigthis.com
"""

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


class FilterReq(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Model for Filter Request
    """


    class MetaOapg:
        
        class properties:
            
            
            class comparison_op(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "allof": "ALLOF",
                        "anyof": "ANYOF",
                        "blank": "BLANK",
                        "btw": "BTW",
                        "checked": "CHECKED",
                        "empty": "EMPTY",
                        "eq": "EQ",
                        "ge": "GE",
                        "gt": "GT",
                        "gte": "GTE",
                        "in": "IN",
                        "is": "IS",
                        "isWithin": "IS_WITHIN",
                        "isnot": "ISNOT",
                        "le": "LE",
                        "like": "LIKE",
                        "lt": "LT",
                        "lte": "LTE",
                        "nallof": "NALLOF",
                        "nanyof": "NANYOF",
                        "nbtw": "NBTW",
                        "neq": "NEQ",
                        "nlike": "NLIKE",
                        "not": "NOT",
                        "notblank": "NOTBLANK",
                        "notchecked": "NOTCHECKED",
                        "notempty": "NOTEMPTY",
                        "notnull": "NOTNULL",
                        "null": "NONE",
                    }
                
                @schemas.classproperty
                def ALLOF(cls):
                    return cls("allof")
                
                @schemas.classproperty
                def ANYOF(cls):
                    return cls("anyof")
                
                @schemas.classproperty
                def BLANK(cls):
                    return cls("blank")
                
                @schemas.classproperty
                def BTW(cls):
                    return cls("btw")
                
                @schemas.classproperty
                def CHECKED(cls):
                    return cls("checked")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("empty")
                
                @schemas.classproperty
                def EQ(cls):
                    return cls("eq")
                
                @schemas.classproperty
                def GE(cls):
                    return cls("ge")
                
                @schemas.classproperty
                def GT(cls):
                    return cls("gt")
                
                @schemas.classproperty
                def GTE(cls):
                    return cls("gte")
                
                @schemas.classproperty
                def IN(cls):
                    return cls("in")
                
                @schemas.classproperty
                def IS(cls):
                    return cls("is")
                
                @schemas.classproperty
                def IS_WITHIN(cls):
                    return cls("isWithin")
                
                @schemas.classproperty
                def ISNOT(cls):
                    return cls("isnot")
                
                @schemas.classproperty
                def LE(cls):
                    return cls("le")
                
                @schemas.classproperty
                def LIKE(cls):
                    return cls("like")
                
                @schemas.classproperty
                def LT(cls):
                    return cls("lt")
                
                @schemas.classproperty
                def LTE(cls):
                    return cls("lte")
                
                @schemas.classproperty
                def NALLOF(cls):
                    return cls("nallof")
                
                @schemas.classproperty
                def NANYOF(cls):
                    return cls("nanyof")
                
                @schemas.classproperty
                def NBTW(cls):
                    return cls("nbtw")
                
                @schemas.classproperty
                def NEQ(cls):
                    return cls("neq")
                
                @schemas.classproperty
                def NLIKE(cls):
                    return cls("nlike")
                
                @schemas.classproperty
                def NOT(cls):
                    return cls("not")
                
                @schemas.classproperty
                def NOTBLANK(cls):
                    return cls("notblank")
                
                @schemas.classproperty
                def NOTCHECKED(cls):
                    return cls("notchecked")
                
                @schemas.classproperty
                def NOTEMPTY(cls):
                    return cls("notempty")
                
                @schemas.classproperty
                def NOTNULL(cls):
                    return cls("notnull")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("null")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'comparison_op':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class comparison_sub_op(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "daysAgo": "DAYS_AGO",
                        "daysFromNow": "DAYS_FROM_NOW",
                        "exactDate": "EXACT_DATE",
                        "nextMonth": "NEXT_MONTH",
                        "nextNumberOfDays": "NEXT_NUMBER_OF_DAYS",
                        "nextWeek": "NEXT_WEEK",
                        "nextYear": "NEXT_YEAR",
                        "oneMonthAgo": "ONE_MONTH_AGO",
                        "oneMonthFromNow": "ONE_MONTH_FROM_NOW",
                        "oneWeekAgo": "ONE_WEEK_AGO",
                        "oneWeekFromNow": "ONE_WEEK_FROM_NOW",
                        "pastMonth": "PAST_MONTH",
                        "pastNumberOfDays": "PAST_NUMBER_OF_DAYS",
                        "pastWeek": "PAST_WEEK",
                        "pastYear": "PAST_YEAR",
                        "today": "TODAY",
                        "tomorrow": "TOMORROW",
                        "yesterday": "YESTERDAY",
                    }
                
                @schemas.classproperty
                def DAYS_AGO(cls):
                    return cls("daysAgo")
                
                @schemas.classproperty
                def DAYS_FROM_NOW(cls):
                    return cls("daysFromNow")
                
                @schemas.classproperty
                def EXACT_DATE(cls):
                    return cls("exactDate")
                
                @schemas.classproperty
                def NEXT_MONTH(cls):
                    return cls("nextMonth")
                
                @schemas.classproperty
                def NEXT_NUMBER_OF_DAYS(cls):
                    return cls("nextNumberOfDays")
                
                @schemas.classproperty
                def NEXT_WEEK(cls):
                    return cls("nextWeek")
                
                @schemas.classproperty
                def NEXT_YEAR(cls):
                    return cls("nextYear")
                
                @schemas.classproperty
                def ONE_MONTH_AGO(cls):
                    return cls("oneMonthAgo")
                
                @schemas.classproperty
                def ONE_MONTH_FROM_NOW(cls):
                    return cls("oneMonthFromNow")
                
                @schemas.classproperty
                def ONE_WEEK_AGO(cls):
                    return cls("oneWeekAgo")
                
                @schemas.classproperty
                def ONE_WEEK_FROM_NOW(cls):
                    return cls("oneWeekFromNow")
                
                @schemas.classproperty
                def PAST_MONTH(cls):
                    return cls("pastMonth")
                
                @schemas.classproperty
                def PAST_NUMBER_OF_DAYS(cls):
                    return cls("pastNumberOfDays")
                
                @schemas.classproperty
                def PAST_WEEK(cls):
                    return cls("pastWeek")
                
                @schemas.classproperty
                def PAST_YEAR(cls):
                    return cls("pastYear")
                
                @schemas.classproperty
                def TODAY(cls):
                    return cls("today")
                
                @schemas.classproperty
                def TOMORROW(cls):
                    return cls("tomorrow")
                
                @schemas.classproperty
                def YESTERDAY(cls):
                    return cls("yesterday")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'comparison_sub_op':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def fk_column_id() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def fk_parent_id() -> typing.Type['StringOrNull']:
                return StringOrNull
        
            @staticmethod
            def is_group() -> typing.Type['ModelBool']:
                return ModelBool
            
            
            class logical_op(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AND(cls):
                    return cls("and")
                
                @schemas.classproperty
                def NOT(cls):
                    return cls("not")
                
                @schemas.classproperty
                def OR(cls):
                    return cls("or")
            value = schemas.AnyTypeSchema
            __annotations__ = {
                "comparison_op": comparison_op,
                "comparison_sub_op": comparison_sub_op,
                "fk_column_id": fk_column_id,
                "fk_parent_id": fk_parent_id,
                "is_group": is_group,
                "logical_op": logical_op,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comparison_op"]) -> MetaOapg.properties.comparison_op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comparison_sub_op"]) -> MetaOapg.properties.comparison_sub_op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_column_id"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fk_parent_id"]) -> 'StringOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_group"]) -> 'ModelBool': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logical_op"]) -> MetaOapg.properties.logical_op: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["comparison_op", "comparison_sub_op", "fk_column_id", "fk_parent_id", "is_group", "logical_op", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comparison_op"]) -> typing.Union[MetaOapg.properties.comparison_op, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comparison_sub_op"]) -> typing.Union[MetaOapg.properties.comparison_sub_op, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_column_id"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fk_parent_id"]) -> typing.Union['StringOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_group"]) -> typing.Union['ModelBool', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logical_op"]) -> typing.Union[MetaOapg.properties.logical_op, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["comparison_op", "comparison_sub_op", "fk_column_id", "fk_parent_id", "is_group", "logical_op", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        comparison_op: typing.Union[MetaOapg.properties.comparison_op, None, str, schemas.Unset] = schemas.unset,
        comparison_sub_op: typing.Union[MetaOapg.properties.comparison_sub_op, None, str, schemas.Unset] = schemas.unset,
        fk_column_id: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        fk_parent_id: typing.Union['StringOrNull', schemas.Unset] = schemas.unset,
        is_group: typing.Union['ModelBool', schemas.Unset] = schemas.unset,
        logical_op: typing.Union[MetaOapg.properties.logical_op, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilterReq':
        return super().__new__(
            cls,
            *args,
            comparison_op=comparison_op,
            comparison_sub_op=comparison_sub_op,
            fk_column_id=fk_column_id,
            fk_parent_id=fk_parent_id,
            is_group=is_group,
            logical_op=logical_op,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from noco_db_python_sdk.model.model_bool import ModelBool
from noco_db_python_sdk.model.string_or_null import StringOrNull
