import logging
from fastapi.responses import JSONResponse
from persistance.models import PlaceModel
from persistance.repository import Repository
from logic.main import build_routes_by_coordinates


class Routers:

    def __init__(self, repository: Repository) -> None:
        self.repository = repository

    async def load_coordinates_to_bd(
            self,
            place_name,
            latitude,
            longitude,
    ):
        try:
            place = PlaceModel(
                place_name=place_name,
                latitude=latitude,
                longitude=longitude,
            )
            self.repository.write_to_db(place)
            return JSONResponse({'Status': 'Success'})
        except Exception as exc:
            logging.error(f'Error {exc}')
            return JSONResponse({'Status': 'Error'})

    def build_routes(
            self,
    ):
        try:
            coordinates = self.repository.get_all_coordinates()
            build_routes_by_coordinates(coordinates)
            return JSONResponse({'Status': 'Success'})
        except Exception as exc:
            logging.error(f'Error {exc}')
            return JSONResponse({'Status': 'Error'})
