# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EnumClass(str, Enum):
    """
    EnumClass
    """

    """
    allowed enum values
    """
    ABC = '_abc'
    MINUS_EFG = '-efg'
    LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS = '(xyz)'

    @classmethod
    def from_json(cls, json_str: str) -> EnumClass:
        """Create an instance of EnumClass from a JSON string"""
        return EnumClass(json.loads(json_str))


    #
    @classmethod
    def _missing_value_(cls, value):
        if value is no_arg:
            return cls.'-efg'

