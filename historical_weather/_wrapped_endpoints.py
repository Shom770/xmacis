from ast import literal_eval
from datetime import datetime
import typing

import lazex
import requests


_SESSION = requests.Session()


class Data:
    """Contains the data retrieved from the xmacis API."""

    def __init__(self, **kwargs):
        for element, value in kwargs.items():
            setattr(self, element.lower(), literal_eval(value))

    def __repr__(self):
        represent_instance = "Data("

        for attr_name, attr_value in vars(self).items():
            represent_instance += f"{attr_name}={attr_value}, "

        return represent_instance.removesuffix(", ") + ")"

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
        (station_id, start_date, end_date, date, ",".join(element.value for element in elements))
    ) if param_value}

    response = _SESSION.get("http://data.rcc-acis.org/StnData", params=parameters).json()

get_station_data("DCA", [__import__("elements").Elements.SNOW, __import__("elements").Elements.MAXIMUM_TEMPERATURE], date=datetime(2022, 1, 3))
