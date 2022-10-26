"""Views module."""

from typing import List

from aiohttp import web
from dependency_injector.wiring import inject, Provide

from src.services import SearchService
from .containers import ApplicationContainer


@inject
async def index(
    request: web.Request,
    search_service: SearchService = Provide[ApplicationContainer.search_service],
    default_query: str = Provide[ApplicationContainer.config.default.query],
    default_limit: int = Provide[ApplicationContainer.config.default.limit.as_int()],
) -> web.Response:
    query = request.query.get('query', default_query)
    limit: int = int(request.query.get('limit', default_limit))

    gifs: List = await search_service.search(query=query, limit=limit)

    return web.json_response(
        data={
            'query': query,
            'limit': limit,
            'gifs': gifs,
        },
    )
