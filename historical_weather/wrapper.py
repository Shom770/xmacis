"""Defines the functions that wrap around the XMACIS API."""
from ast import literal_eval
from datetime import datetime
from typing import Sequence, Any

from requests import session
from .codes import Element, ElementType
from .errors import IncorrectParametersError

__all__ = ["get_station_data"]

BASE_URL = "https://data.rcc-acis.org"
SESSION = session()


def _convert_to_python_type(to_convert: str) -> Any:
    """Helper function to convert the data XMACIS returns into their respective Python type.

    :param to_convert: The datum to convert into a proper type.
    """
    try:
        return datetime.strptime(to_convert, "%Y-%m-%d")
    except ValueError:
        try:
            return literal_eval(to_convert)
        except ValueError:
            return to_convert


def get_station_data(
    station_id: str,
    *,
    start_date: datetime | str = None,
    end_date: datetime | str = None,
    date: datetime | str = None,
    elements: Sequence[Element] | Sequence[ElementType] | Sequence[str] | Sequence[dict] | Element | ElementType = None,
    convert_to_their_types: bool = False,
):
    """Retrieves data from a single station using the RCC ACIS API.

    :param station_id: The station ID to retrieve the data from (eg. KIAD)
    :param start_date: The date to begin retrieving the data from (optional if you pass in a date).
    :param end_date: The date to stop retrieving the data from (optional if you pass in a date).
    :param date: The single day to retrieve data from (optional if you pass in a start date and end date).
    :param elements: The elements to retrieve in data (like snow, precipitation, etc.)
    :param convert_to_their_types: Whether or not to convert to their respective types from a string at the end of retrieving the data.
    :return:
    """
    # None of the date parameters were passed in.
    if not start_date and not end_date and not date:
        raise IncorrectParametersError(
            f"{start_date=}, {end_date=}, and {date=}"
            f". You need to pass in either a single date or a start date and end date."
        )

    # All of the date parameters were passed in.
    if start_date and end_date and date:
        raise IncorrectParametersError(
            f"{start_date=}, {end_date=} and {date=}. You need to either pass in a start date or end date,"
            f" or a date only. You can't pass in all three parameters."
        )

    # No elements were passed in
    if not elements:
        raise IncorrectParametersError(f"{elements=}. You need to pass in at least one element.")

    # Build the parameters for the API request.
    parameters = {"sid": station_id}

    if start_date and end_date:
        parameters["sdate"] = (start_date.strftime("%Y-%m-%d") if isinstance(start_date, datetime) else start_date)
        parameters["edate"] = (end_date.strftime("%Y-%m-%d") if isinstance(end_date, datetime) else end_date)
    else:
        parameters["date"] = (date.strftime('%Y-%m-%d') if isinstance(date, datetime) else date)

    # Handle the different types of elements passed in.
    if isinstance(elements, Element):
        parameters["elems"] = [elements.as_dict()]
    elif isinstance(elements, ElementType):
        parameters["elems"] = elements.value
    elif isinstance(elements[0], Element):
        parameters["elems"] = [element.as_dict() for element in elements]
    elif isinstance(elements[0], dict):
        parameters["elems"] = elements
    elif isinstance(elements[0], str):
        parameters["elems"] = ",".join(elements)
    else:
        parameters["elems"] = ",".join(element.value for element in elements)

    # API call
    response = SESSION.post(f"{BASE_URL}/StnData", json=parameters).json()

    if convert_to_their_types:
        response["data"] = [
            [_convert_to_python_type(value) if value != "M" else float("nan") for value in values]
            for values in response["data"]
        ]

    return response
