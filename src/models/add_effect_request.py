# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AddEffectRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AddEffectRequest - a model defined in OpenAPI

        title: The title of this AddEffectRequest.
        title_en: The title_en of this AddEffectRequest [Optional].
        subtitle: The subtitle of this AddEffectRequest.
        subtitle_en: The subtitle_en of this AddEffectRequest [Optional].
        author: The author of this AddEffectRequest.
        author_en: The author_en of this AddEffectRequest [Optional].
        description: The description of this AddEffectRequest.
        description_en: The description_en of this AddEffectRequest [Optional].
        thumbnail: The thumbnail of this AddEffectRequest.
        data: The data of this AddEffectRequest.
    """

    title: str
    title_en: Optional[str] = None
    subtitle: str
    subtitle_en: Optional[str] = None
    author: str
    author_en: Optional[str] = None
    description: str
    description_en: Optional[str] = None
    thumbnail: str
    data: str

    @validator("title")
    def title_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("title")
    def title_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("title_en")
    def title_en_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("subtitle")
    def subtitle_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("subtitle")
    def subtitle_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("subtitle_en")
    def subtitle_en_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("author")
    def author_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("author")
    def author_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("author_en")
    def author_en_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value

    @validator("description_en")
    def description_en_max_length(cls, value):
        assert len(value) <= 3000
        return value

AddEffectRequest.update_forward_refs()
