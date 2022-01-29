# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.sonolus_resource_locator import SonolusResourceLocator


class Effect(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Effect - a model defined in OpenAPI

        name: The name of this Effect [Optional].
        version: The version of this Effect [Optional].
        title: The title of this Effect [Optional].
        titleEn: The titleEn of this Effect [Optional].
        subtitle: The subtitle of this Effect [Optional].
        subtitleEn: The subtitleEn of this Effect [Optional].
        author: The author of this Effect [Optional].
        authorEn: The authorEn of this Effect [Optional].
        description: The description of this Effect [Optional].
        descriptionEn: The descriptionEn of this Effect [Optional].
        thumbnail: The thumbnail of this Effect [Optional].
        data: The data of this Effect [Optional].
        createdTime: The createdTime of this Effect [Optional].
        updatedTime: The updatedTime of this Effect [Optional].
        userId: The userId of this Effect [Optional].
        public: The public of this Level [Optional].
    """

    name: Optional[str] = None
    version: Optional[int] = None
    title: Optional[str] = None
    titleEn: Optional[str] = None
    subtitle: Optional[str] = None
    subtitleEn: Optional[str] = None
    author: Optional[str] = None
    authorEn: Optional[str] = None
    description: Optional[str] = None
    descriptionEn: Optional[str] = None
    thumbnail: Optional[SonolusResourceLocator] = None
    data: Optional[SonolusResourceLocator] = None
    createdTime: Optional[int] = None
    updatedTime: Optional[int] = None
    userId: Optional[str] = None
    public: Optional[bool] = None

    @validator("name")
    def name_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("name")
    def name_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("version")
    def version_max(cls, value):
        assert value <= 100
        return value

    @validator("version")
    def version_min(cls, value):
        assert value >= 1
        return value

    @validator("title")
    def title_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("title")
    def title_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("titleEn")
    def titleEn_min_length(cls, value):
        assert len(value) >= 0
        return value

    @validator("titleEn")
    def titleEn_max_length(cls, value):
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

    @validator("subtitleEn")
    def subtitleEn_min_length(cls, value):
        assert len(value) >= 0
        return value

    @validator("subtitleEn")
    def subtitleEn_max_length(cls, value):
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

    @validator("authorEn")
    def authorEn_min_length(cls, value):
        assert len(value) >= 0
        return value

    @validator("authorEn")
    def authorEn_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("description")
    def description_min_length(cls, value):
        assert len(value) >= 0
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value

    @validator("descriptionEn")
    def descriptionEn_min_length(cls, value):
        assert len(value) >= 0
        return value

    @validator("descriptionEn")
    def descriptionEn_max_length(cls, value):
        assert len(value) <= 3000
        return value

    @validator("createdTime")
    def createdTime_min(cls, value):
        assert value >= 0
        return value

    @validator("updatedTime")
    def updatedTime_min(cls, value):
        assert value >= 0
        return value

    @validator("userId")
    def userId_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("userId")
    def userId_max_length(cls, value):
        assert len(value) <= 100
        return value


Effect.update_forward_refs()
