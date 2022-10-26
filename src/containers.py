"""Application containers module."""

from dependency_injector import containers, providers

from src import giphy, services


class ApplicationContainer(containers.DeclarativeContainer):
    """Application container."""

    wiring_config = containers.WiringConfiguration(modules=['.handlers'])

    config = providers.Configuration(yaml_files=['config.yml'])

    giphy_client = providers.Factory(
        provides=giphy.GiphyClient,
        api_key=config.giphy.api_key,
        timeout=config.giphy.request_timeout,
    )

    search_service = providers.Factory(
        provides=services.SearchService,
        giphy_client=giphy_client,
    )
