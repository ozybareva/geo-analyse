from injector import provider, singleton, Module

from persistance.postgres_connection import PostgresConnector
from persistance.repository import Repository
from application.routers import Routers
from settings import Settings


class Container(Module):

    @provider
    @singleton
    def provide_settings(self) -> Settings:
        return Settings()

    @provider
    @singleton
    def provide_postgres_connection(self, settings: Settings) -> PostgresConnector:
        return PostgresConnector(settings)

    @provider
    @singleton
    def provide_repository(self, postgres: PostgresConnector) -> Repository:
        return Repository(postgres)

    @provider
    @singleton
    def provide_message_router(
            self,
            repository: Repository
    ) -> Routers:
        return Routers(repository)

