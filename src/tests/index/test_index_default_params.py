import http
from unittest import mock

import pytest

from src.giphy import GiphyClient


@pytest.mark.asyncio
async def test_index_default_params(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        'data': [],
    }
    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get('/')

    assert response.status == http.HTTPStatus.OK
    data = await response.json()
    assert data['query'] == app.container.config.default.query()
    assert data['limit'] == app.container.config.default.limit()
