# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class SearchSliderOption(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SearchSliderOption - a model defined in OpenAPI

        query: The query of this SearchSliderOption.
        name: The name of this SearchSliderOption.
        type: The type of this SearchSliderOption.
        _def: The _def of this SearchSliderOption.
        min: The min of this SearchSliderOption.
        max: The max of this SearchSliderOption.
        step: The step of this SearchSliderOption.
        display: The display of this SearchSliderOption.
    """

    query: str
    name: str
    type: str
    _def: int
    min: int
    max: int
    step: int
    display: str

    @validator("_def")
    def _def_min(cls, value):
        assert value >= 0
        return value

    @validator("min")
    def min_min(cls, value):
        assert value >= 0
        return value

    @validator("max")
    def max_min(cls, value):
        assert value >= 0
        return value

    @validator("step")
    def step_min(cls, value):
        assert value >= 0
        return value

SearchSliderOption.update_forward_refs()