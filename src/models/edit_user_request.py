# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class EditUserRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EditUserRequest - a model defined in OpenAPI

        test_id: The test_id of this EditUserRequest [Optional].
        account_id: The account_id of this EditUserRequest [Optional].
        description: The description of this EditUserRequest [Optional].
    """

    test_id: Optional[str] = None
    account_id: Optional[str] = None
    description: Optional[str] = None

    @validator("test_id")
    def test_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("test_id")
    def test_id_max_length(cls, value):
        assert len(value) <= 30
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value

EditUserRequest.update_forward_refs()
