"""Tests module."""
import pytest

from src.application import create_app


@pytest.fixture
def app():
    app = create_app()
    yield app
    app.container.unwire()


@pytest.fixture
def client(app, aiohttp_client, event_loop):
    return event_loop.run_until_complete(aiohttp_client(app))
