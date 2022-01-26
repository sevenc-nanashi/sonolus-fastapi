# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.effect import Effect


class GetEffectResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetEffectResponse - a model defined in OpenAPI

        item: The item of this GetEffectResponse.
        description: The description of this GetEffectResponse.
        recommended: The recommended of this GetEffectResponse.
    """

    item: Effect
    description: str
    recommended: List[Effect]

    @validator("description")
    def description_min_length(cls, value):
        assert len(value) >= 0
        return value


GetEffectResponse.update_forward_refs()
