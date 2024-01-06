from typing import NoReturn

import datastore as ds


def test_get_forecasts() -> NoReturn:
    forecast_records = ds.ForecastDB.get_all_forecasts()
    assert isinstance(forecast_records, list)
    assert len(forecast_records) == 1000


def test_get_forecast_by_id() -> NoReturn:
    forecast_record = ds.ForecastDB.get_all_forecasts()[0]
    assert forecast_record == ds.ForecastDB.find_forecast_by_id(forecast_record.id)
