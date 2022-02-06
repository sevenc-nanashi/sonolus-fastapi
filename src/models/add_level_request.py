# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AddLevelRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AddLevelRequest - a model defined in OpenAPI

        rating: The rating of this AddLevelRequest.
        engine: The engine of this AddLevelRequest.
        skin: The skin of this AddLevelRequest [Optional].
        background: The background of this AddLevelRequest [Optional].
        effect: The effect of this AddLevelRequest [Optional].
        particle: The particle of this AddLevelRequest [Optional].
        title: The title of this AddLevelRequest.
        titleEn: The titleEn of this AddLevelRequest [Optional].
        artists: The artists of this AddLevelRequest.
        artistsEn: The artistsEn of this AddLevelRequest [Optional].
        author: The author of this AddLevelRequest.
        authorEn: The authorEn of this AddLevelRequest [Optional].
        description: The description of this AddLevelRequest.
        descriptionEn: The descriptionEn of this AddLevelRequest [Optional].
        cover: The cover of this AddLevelRequest.
        bgm: The bgm of this AddLevelRequest.
        data: The data of this AddLevelRequest.
        preview: The preview of this AddLevelRequest.
        genre: The genre of this AddLevelRequest.
        length: The length of this AddLevelRequest.
        bpm: The bpm of this AddLevelRequest.
        notes: The notes of this AddLevelRequest.
    """

    rating: int
    engine: str
    skin: Optional[str] = None
    background: Optional[str] = None
    effect: Optional[str] = None
    particle: Optional[str] = None
    title: str
    titleEn: Optional[str] = None
    artists: str
    artistsEn: Optional[str] = None
    author: str
    authorEn: Optional[str] = None
    description: str
    descriptionEn: Optional[str] = None
    cover: str
    bgm: str
    data: str
    preview: str
    genre: list[str]
    length: int
    bpm: int
    notes: int

    @validator("rating")
    def rating_max(cls, value):
        assert value <= 100
        return value

    @validator("rating")
    def rating_min(cls, value):
        assert value >= 1
        return value

    @validator("engine")
    def engine_max_length(cls, value):
        assert len(value) <= 50
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

    @validator("artists")
    def artists_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("artists")
    def artists_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("artistsEn")
    def artistsEn_max_length(cls, value):
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

    @validator("cover")
    def cover_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("bgm")
    def bgm_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("data")
    def data_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("preview")
    def preview_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("length")
    def length_max(cls, value):
        assert value <= 99999
        return value

    @validator("length")
    def length_min(cls, value):
        assert value >= 0
        return value

    @validator("bpm")
    def bpm_max(cls, value):
        assert value <= 10000
        return value

    @validator("bpm")
    def bpm_min(cls, value):
        assert value >= 0
        return value

    @validator("notes")
    def notes_max(cls, value):
        assert value <= 10000000
        return value

    @validator("notes")
    def notes_min(cls, value):
        assert value >= 1
        return value


AddLevelRequest.update_forward_refs()