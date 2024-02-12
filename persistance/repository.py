from sqlalchemy import select
from persistance.postgres_connection import PostgresConnector
from persistance.models import PlaceModel


class Repository:
    def __init__(self, postgres: PostgresConnector):
        self.postgres_session = postgres.get_session()
        postgres.declare_base()

    def write_to_db(self, model):
        self.postgres_session.add(model)
        self.postgres_session.commit()

    async def get_coordinates_by_name(self, place_name: str):
        stmt = select(PlaceModel.latitude, PlaceModel.latitude)\
            .filter(PlaceModel.place_name is place_name)
        return self.postgres_session.scalar(stmt)
