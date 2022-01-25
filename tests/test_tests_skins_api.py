# coding: utf-8

from typing import Dict

from fastapi.testclient import TestClient
from src.models.get_skin_list_response import GetSkinListResponse  # noqa: F401
from src.models.get_skin_response import GetSkinResponse  # noqa: F401


def test_get_skin_test(client: TestClient) -> None:
    """Test case for get_skin_test

    Get tests skin
    """

    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/skins/{skinName}".format(
            testId="test_id_example", skinName="skin_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


def test_get_tests_skins(client: TestClient) -> None:
    """Test case for get_tests_skins

    Get tests skin list
    """
    params: Dict[str, str] = dict(
        [("localization", "en"), ("page", "1"), ("keywords", "Redo")]
    )
    headers: Dict[str, str] = {}
    response = client.request(
        "GET",
        "/tests/{testId}/skins/list".format(testId="test_id_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500