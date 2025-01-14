# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.background import Background
from src.models.search import Search


class GetBackgroundListResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetBackgroundListResponse - a model defined in OpenAPI

        pageCount: The pageCount of this GetBackgroundListResponse.
        items: The items of this GetBackgroundListResponse.
        search: The search of this GetBackgroundListResponse.
    """

    pageCount: int
    items: List[Background]
    search: Search

    @validator("pageCount")
    def pageCount_min(cls, value):
        assert value >= 1
        return value

GetBackgroundListResponse.update_forward_refs()
