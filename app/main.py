import logging
from typing import List

import datastore as ds
from fastapi import FastAPI, HTTPException

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
app = FastAPI()


@app.get('/health')
def health():
    pass


@app.get('/api/forecasts')
def get_forecasts(city: str = None,
                  min_temperature: int = None,
                  max_temperature: int = None) -> List[ds.ForecastRecord]:
    logging.info(
        f'Request /api/forecasts?city={city}&min_temperature={min_temperature}&max_temperature={max_temperature}')
    return ds.ForecastDB.get_forecasts(city, min_temperature, max_temperature)


@app.get('/api/forecasts/{forecast_id}')
def get_forecast_by_id(forecast_id: str) -> ds.ForecastRecord:
    logging.info(f'Request /api/forecasts/{forecast_id}')
    try:
        return ds.ForecastDB.find_forecast_by_id(forecast_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail='Item not found')
