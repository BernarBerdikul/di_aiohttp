"""Giphy client module."""
import http

from aiohttp import ClientSession, ClientTimeout


class GiphyClient:

    API_URL: str = 'https://api.giphy.com/v1'

    def __init__(self, api_key: str, timeout: int):
        self._api_key = api_key
        self._timeout = ClientTimeout(timeout)

    async def search(self, query, limit: int):
        """Make search API call and return result."""
        url: str = f'{self.API_URL}/gifs/search'
        params = {
            'q': query,
            'api_key': self._api_key,
            'limit': limit,
        }
        async with ClientSession(timeout=self._timeout) as session:
            async with session.get(url, params=params) as response:
                if response.status != http.HTTPStatus.OK:
                    response.raise_for_status()
                return await response.json()
