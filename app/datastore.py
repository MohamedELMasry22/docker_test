import uuid
from typing import List, Optional

from pydantic import BaseModel, Field


class ForecastRecord(BaseModel):
    id: str = Field(title='Id of forecast record)')
    source_id: str = Field(title='Id of the source device (Sensor Id for example)')
    timestamp: str = Field(title='Timestamp')
    city: str = Field(title='City name')
    temperature: int = Field(title='Temperature in celsius')
    visibility: int = Field(title='Visibility percentage 0-100%', ge=0, le=100)
    wind_speed: int = Field(title='Wind speed KmH', ge=0)
    humidity: int = Field(title='Humidity', description='Humidity percentage 0-100%', ge=0, le=100)


def random_city():
    import random
    return random.choice([
        'Abu Dhabi',
        'Amman',
        'Ankara',
        'Berlin',
        'Bangkok',
        'Buenos Aires',
        'Canberra',
        'Ciro',
        'Copenhagen',
        'Dublin',
        'Doha',
        'Damascus',
        'London',
        'Manila',
        'Moscow',
        'Oslo',
        'Paris',
        'Rome',
        'Sofia',
        'Tokyo',
        'Washington D.C.'
    ])


def generate_forecast_data(length: int = 100) -> List[ForecastRecord]:
    import datetime
    import random

    return [ForecastRecord(id=str(uuid.uuid4()),
                           source_id=str(uuid.uuid4()),
                           timestamp='{:%Y-%m-%dT%H:%M:%S}'.format(datetime.datetime.now()),
                           city=random_city(),
                           temperature=random.randint(-10, 35),
                           visibility=random.randint(0, 100),
                           wind_speed=random.randint(0, 120),
                           humidity=random.randint(5, 70))
            for _ in range(length)]


class ForecastDB:
    __forecast_db: List[ForecastRecord] = generate_forecast_data(1000)

    @staticmethod
    def get_all_forecasts() -> List[ForecastRecord]:
        return ForecastDB.get_forecasts(city=None, min_temperature=None, max_temperature=None)

    @staticmethod
    def get_forecasts(city: str, min_temperature: int, max_temperature: int) -> List[ForecastRecord]:
        return list(filter(lambda forecast: (city is None or forecast.city == city)
                           and (min_temperature is None or min_temperature <= forecast.temperature)
                           and (max_temperature is None or max_temperature >= forecast.temperature),
                           ForecastDB.__forecast_db))

    @staticmethod
    def find_forecast_by_id(forecast_id: str) -> Optional[ForecastRecord]:
        return next(filter(lambda forecast_record: forecast_record.id == forecast_id, ForecastDB.__forecast_db))
