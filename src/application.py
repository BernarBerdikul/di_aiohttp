"""Application module."""

from aiohttp import web

from .containers import ApplicationContainer
from . import handlers


def create_app() -> web.Application:
    """Create and return aiohttp application."""
    container = ApplicationContainer()
    container.config.giphy.api_key.from_env('GIPHY_API_KEY')

    app = web.Application()
    app.container = container
    app.add_routes([
        web.get('/', handlers.index)
    ])
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app=app)
