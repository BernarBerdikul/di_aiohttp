import http
from unittest import mock

import pytest

from src.giphy import GiphyClient


@pytest.mark.asyncio
async def test_index(client, app):
    giphy_client_mock = mock.AsyncMock(spec=GiphyClient)
    giphy_client_mock.search.return_value = {
        'data': [
            {'url': 'https://giphy.com/gif1.gif'},
            {'url': 'https://giphy.com/gif2.gif'},
        ],
    }
    with app.container.giphy_client.override(giphy_client_mock):
        response = await client.get(
            '/',
            params={
                'query': 'test',
                'limit': 10,
            }
        )
    assert response.status == http.HTTPStatus.OK
    data = await response.json()
    assert data == {
        'query': 'test',
        'limit': 10,
        'gifs': [
            {'url': 'https://giphy.com/gif1.gif'},
            {'url': 'https://giphy.com/gif2.gif'},
        ]
    }
