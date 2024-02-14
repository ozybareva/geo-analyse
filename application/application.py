import asyncio
import logging
import uvicorn

from injector import Injector
from fastapi import FastAPI

from application.routers import Routers
from settings import Settings


class App:

    def __init__(self, container):
        self.container = Injector(container)
        self.app = FastAPI()
        self.loop = asyncio.get_event_loop()
        self.server = self.init_server(self.loop)
        self.settings = self.container.get(Settings)
        self.routers = self.container.get(Routers)

    def start(self):

        self.add_routes()

        try:
            logging.info(f'Start application')
            tasks = asyncio.gather(
                self.server.serve(),
            )
            self.loop.run_until_complete(tasks)

            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        except Exception:
            logging.error('Unexpected error')
        finally:
            self.loop.close()

    def init_server(self, loop):
        config = uvicorn.Config(app=self.app,
                                loop=loop,
                                host='0.0.0.0')

        return uvicorn.Server(config)

    def add_routes(self):
        self.app.add_api_route(
            '/add_place',
            self.routers.load_coordinates_to_bd,
            methods=['POST']
        )
        self.app.add_api_route(
            '/build_routes',
            self.routers.build_routes,
            methods=['POST']
        )
