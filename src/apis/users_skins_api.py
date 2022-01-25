# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)
from src.apis.depends import (
    dependsKeywords,
    dependsLocalization,
    dependsPage,
    dependsPath,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_skin_list_response import GetSkinListResponse
from src.models.get_skin_response import GetSkinResponse

router = APIRouter()


@router.get(
    "/users/{userId}/skins/{skinName}",
    responses={
        200: {"model": GetSkinResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["users_skins"],
    summary="Get users skin",
)
async def get_users_skin(
    userId: str = dependsPath,
    skinName: str = dependsPath,
) -> GetSkinResponse:
    """It returns specified skin info.
    It will raise 404 if the skin is not registered in this server"""
    ...


@router.get(
    "/users/{userId}/skins/list",
    responses={
        200: {"model": GetSkinListResponse, "description": "OK"},
    },
    tags=["users_skins"],
    summary="Get users skin list",
)
async def get_users_skins(
    userId: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
) -> GetSkinListResponse:
    """ユーザー個別用エンドポイント/ スキン一覧を返す"""
    ...
