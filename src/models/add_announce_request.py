# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AddAnnounceRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AddAnnounceRequest - a model defined in OpenAPI

        name: The name of this AddAnnounceRequest.
        rating: The rating of this AddAnnounceRequest [Optional].
        title: The title of this AddAnnounceRequest.
        titleEn: The titleEn of this AddAnnounceRequest [Optional].
        subtitle: The subtitle of this AddAnnounceRequest.
        subtitleEn: The subtitleEn of this AddAnnounceRequest [Optional].
        author: The author of this AddAnnounceRequest.
        authorEn: The authorEn of this AddAnnounceRequest [Optional].
        description: The description of this AddAnnounceRequest.
        descriptionEn: The descriptionEn of this AddAnnounceRequest [Optional].
        cover: The cover of this AddAnnounceRequest.
        bgm: The bgm of this AddAnnounceRequest [Optional].
        preview: The preview of this AddAnnounceRequest [Optional].
        public: The public of this AddAnnounceRequest [Optional].
    """

    name: str
    rating: Optional[int] = None
    title: str
    titleEn: Optional[str] = None
    subtitle: str
    subtitleEn: Optional[str] = None
    author: str
    authorEn: Optional[str] = None
    description: str
    descriptionEn: Optional[str] = None
    cover: str
    bgm: Optional[str] = None
    preview: Optional[str] = None
    public: Optional[bool] = None

    @validator("name")
    def name_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("name")
    def name_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("rating")
    def rating_max(cls, value):
        assert value <= 100
        return value

    @validator("rating")
    def rating_min(cls, value):
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
    def authorEn_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value

    @validator("descriptionEn")
    def descriptionEn_max_length(cls, value):
        assert len(value) <= 3000
        return value

AddAnnounceRequest.update_forward_refs()
