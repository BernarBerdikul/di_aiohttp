import http
from unittest import mock

import pytest

from src.giphy import GiphyClient


@pytest.mark.asyncio
async def test_index_no_data(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        'data': [],
    }
    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get('/')

    assert response.status == http.HTTPStatus.OK
    data = await response.json()
    assert data['gifs'] == []
