from typing import Union

import sqlalchemy  # noqa: F401
from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import BACKGROUND_VERSION
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    DataBridge,
    get_current_unix,
    get_first_item_or_404,
    is_owner_or_admin_otherwise_409,
    not_exist_or_409,
    patch_to_model,
    save_to_db,
)
from src.database.objects.background import Background as BackgroundSave
from src.models.background import Background as BackgroundReqResp
from src.models.default_search import defaultSearch
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage

OBJECT_NAME = "background"
LOCATER_NAMES = ["thumbnail", "data", "image", "configuration"]
OBJECT_VERSION = BACKGROUND_VERSION


async def create_background(
    db: AsyncSession, model: BackgroundReqResp, auth: FirebaseClaims
) -> Union[HTTPException, GetBackgroundResponse]:
    """背景を追加します"""
    await not_exist_or_409(
        db,
        select(BackgroundSave).filter(
            BackgroundSave.name == model.name,
        ),
    )
    # 入力を DBに合わせる
    bridge = DataBridge(db, OBJECT_NAME, LOCATER_NAMES, OBJECT_VERSION, auth, True)
    await bridge.to_db(model)
    background_db = BackgroundSave(**model.dict())
    await save_to_db(db, background_db)
    bridge.to_resp(background_db)
    item = BackgroundReqResp.from_orm(background_db)
    resp = GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )
    return resp


async def get_background(
    db: AsyncSession, name: str, localization: str
) -> GetBackgroundResponse:
    """背景を取得します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db, select(BackgroundSave).filter(BackgroundSave.userId == name)
    )
    bridge = DataBridge(db, OBJECT_NAME, LOCATER_NAMES, OBJECT_VERSION)
    bridge.to_resp(background_db, localization)
    item = BackgroundReqResp.from_orm(background_db)
    return GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def edit_background(
    db: AsyncSession,
    name: str,
    model: BackgroundReqResp,
    auth: FirebaseClaims,
) -> Union[HTTPException, GetBackgroundResponse]:
    """背景を編集します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db,
        select(BackgroundSave).filter(
            BackgroundSave.name == name,
        ),
    )
    await is_owner_or_admin_otherwise_409(db, background_db, auth)
    bridge = DataBridge(db, OBJECT_NAME, LOCATER_NAMES, OBJECT_VERSION, auth)
    patch_to_model(background_db, model.dict(exclude_unset=True), LOCATER_NAMES, [])
    await save_to_db(db, background_db)
    bridge.to_resp(background_db)
    item = BackgroundReqResp.from_orm(background_db)
    return GetBackgroundResponse(
        item=item,
        description=item.description,
        recommended=[],
    )


async def delete_background(
    db: AsyncSession,
    name: str,
    auth: FirebaseClaims,
) -> Union[HTTPException, None]:
    """背景を削除します"""
    background_db: BackgroundSave = await get_first_item_or_404(
        db, select(BackgroundSave).filter(BackgroundSave.name == name)
    )
    await is_owner_or_admin_otherwise_409(db, background_db, auth)
    background_db.isDeleted = True
    background_db.updatedTime = get_current_unix()
    save_to_db(db, background_db)
    return None


async def list_background(
    db: AsyncSession, page: int, queries: SearchQueries
) -> GetBackgroundListResponse:
    """背景一覧を取得します"""
    select_query = buildDatabaseQuery(BackgroundSave, queries)
    userPage: Page[BackgroundSave] = await paginate(
        db,
        select_query,
        Params(page=page + 1, size=20),
    )  # type: ignore
    bridge = DataBridge(db, OBJECT_NAME, LOCATER_NAMES, OBJECT_VERSION)
    resp: SonolusPage = toSonolusPage(userPage)
    for r in resp.items:
        bridge.to_resp(r, queries.localization)
    return GetBackgroundListResponse(
        pageCount=resp.pageCount if resp.pageCount > 0 else 1,
        items=resp.items,
        search=defaultSearch,
    )