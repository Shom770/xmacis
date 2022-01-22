from datetime import datetime
import typing

import lazex
import requests


_SESSION = requests.Session()


class Data:
    """Contains the data retrieved from the xmacis API."""


def get_station_data(
    station_id: str,
    elements: typing.Optional[typing.Sequence] = None,
    *,
    start_date: typing.Optional[datetime] = None,
    end_date: typing.Optional[datetime] = None,
    date: typing.Optional[datetime] = None,
) -> Data:
    """Retrieves the station data based off the filters provided."""

    parameters = {param_name: param_value.strftime("%Y-%m-%d") if isinstance(param_value, datetime) else param_value
                  for param_name, param_value in zip(
        ("sid", "sdate", "edate", "date", "elems"),
        (station_id, start_date, end_date, date, elements)
    ) if param_value}

    response = _SESSION.get("http://data.rcc-acis.org/StnData", params=parameters).json()
    print(response)

get_station_data("DCA", [__import__("elements").SNOW], date=datetime(2022, 1, 3))
