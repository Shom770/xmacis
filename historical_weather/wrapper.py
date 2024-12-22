"""Defines the functions that wrap around the XMACIS API."""
from ast import literal_eval
from datetime import datetime
from typing import Sequence, Any

from requests import session
from .codes import Element, ElementType
from .errors import IncorrectParametersError
from .utils import calculate_awssi_index

__all__ = ["accumulated_winter_season_severity_index", "get_station_data", "get_multi_station_data"]

BASE_URL = "https://data.rcc-acis.org"
SESSION = session()


def _convert_to_python_type(to_convert: str, avoid_converting_dates: bool) -> Any:
    """Helper function to convert the data XMACIS returns into their respective Python type.

    :param to_convert: The datum to convert into a proper type.
    :param avoid_converting_dates: Whether or not to convert a string into a `datetime` object.
    :return: The proper type that the datum should be converted into.
    """
    if to_convert == "M":
        return float("nan")
    elif to_convert == "T":
        return 0.01

    try:
        converted_date = datetime.strptime(to_convert, "%Y-%m-%d")
        return converted_date if not avoid_converting_dates else to_convert
    except ValueError:
        try:
            return literal_eval(to_convert)
        except (ValueError, SyntaxError):
            return to_convert


def get_station_data(
    station_id: str,
    *,
    start_date: datetime | str = None,
    end_date: datetime | str = None,
    date: datetime | str = None,
    elements: Sequence[Element] | Sequence[ElementType] | Sequence[str] | Sequence[dict] | Element | ElementType = None,
    meta: str | list[str] = (),
    convert_to_their_types: bool = False,
    avoid_converting_dates: bool = False,
    replace_traces_with_integers: bool = False
) -> dict:
    """Retrieves data from a single station using the RCC ACIS API.

    :param station_id: The station ID to retrieve the data from (eg. KIAD)
    :param start_date: The date to begin retrieving the data from (optional if you pass in a date).
    :param end_date: The date to stop retrieving the data from (optional if you pass in a date).
    :param date: The single day to retrieve data from (optional if you pass in a start date and end date).
    :param elements: The elements to retrieve in data (like snow, precipitation, etc.)
    :param meta: The metadata to return from the RCC ACIS API (eg. ["ll", "elev"])
    :param convert_to_their_types: Whether or not to convert to their respective types from a string at the end of retrieving the data.
    :param avoid_converting_dates: If `convert_to_their_types` is true, then this flag determines whether or not dates should be converted into `datetime`.
    :param replace_traces_with_integers: Replaces any `T` in the data with 0.01 for snowfall data. Needs to be used with convert_to_their_types.
    :return: The cleaned up data returned by the RCC ACIS API.
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
    parameters = {"sid": station_id, "meta": meta}

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
    if response.get("data") is None:
        raise ValueError(response.get("error", "An error occured. Maybe try a different station?"))
    if convert_to_their_types:
        response["data"] = [
            [
                _convert_to_python_type(value, avoid_converting_dates)
                if value != "M" else float("nan")
                for value in values
            ]
            for values in response["data"]
        ]

    return response


def get_multi_station_data(
    *,
    county: str | int | list[str] | list[int] = None,
    climdiv: str | list[str] = None,
    cwa: str | list[str] = None,
    basin: str | int | list[str] | list[int] = None,
    state: str | list[str] = None,
    bbox: list[float] = None,
    sids: list[str] = None,
    meta: str | list[str] = (),
    start_date: datetime | str = None,
    end_date: datetime | str = None,
    date: datetime | str = None,
    elements: Sequence[Element] | Sequence[ElementType] | Sequence[str] | Sequence[dict] | Element | ElementType = None,
    convert_to_their_types: bool = False,
    avoid_converting_dates: bool = False,
    unpack_single_value: bool = False
) -> dict:
    """Retrieves data from multiple stations using the RCC ACIS API.

    :param county: One or more county FIPS codes (eg. 09001)
    :param climdiv: One or more state/climate divison identifiers (eg. NY09)
    :param cwa: One or more NWS County Warning Areas (eg. LWX)
    :param basin: One or more drainage basins (eg. 01080205)
    :param state: One or more 2-letter state postal abbreviations (eg. ["MD", "VA"])
    :param bbox: Bounding box specified in decimal degrees (W,S,E,N) (eg. [-90, 40, -88, 41])
    :param sids: One or more station IDs (eg. ["KIAD", "KBWI"])
    :param meta: The metadata to return from the RCC ACIS API (eg. ["ll", "elev"])
    :param start_date: The date to begin retrieving the data from (optional if you pass in a date).
    :param end_date: The date to stop retrieving the data from (optional if you pass in a date).
    :param date: The single day to retrieve data from (optional if you pass in a start date and end date).
    :param elements: The elements to retrieve in data (like snow, precipitation, etc.)
    :param convert_to_their_types: Whether or not to convert to their respective types from a string at the end of retrieving the data.
    :param avoid_converting_dates: If `convert_to_their_types` is true, then this flag determines whether or not dates should be converted into `datetime`.
    :param unpack_single_value: Flag for whether or not to unpack a single element in the data. If you're only recommending a single element, it's recommended you do this.
    :return: The response returned by the request to the MultiStnData endpoint of the RCC ACIS API.
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

    possible_identifiers = [
        ("county", county),
        ("climdiv", climdiv),
        ("cwa", cwa),
        ("basin", basin),
        ("state", state),
        ("bbox", bbox),
        ("sids", sids)
    ]

    # None of the identifiers were passed in.
    if not (county or climdiv or cwa or basin or state or bbox or sids):
        raise IncorrectParametersError(
            "You need to pass in at least one of the following parameters: "
            "county, climdiv, cwa, basin, state, bbox, or sids."
        )

    # More than one of the identifiers were passed in.
    if [bool(value) for _, value in possible_identifiers].count(True) > 1:
        raise IncorrectParametersError(
            "You can only pass in one of the identifiers listed below: "
            "county, climdiv, cwa, basin, state, bbox, or sids."
        )

    identifier_name, identifier = next(pair for pair in possible_identifiers if pair[-1])

    # Build the parameters for the API request.
    parameters = {identifier_name: identifier, "meta": meta}

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
    response = SESSION.post(f"{BASE_URL}/MultiStnData", json=parameters).json()

    if response.get("data") is None:
        raise ValueError(response.get("error", "An error occured. Maybe try a different station?"))

    if convert_to_their_types:
        response["data"] = [
            {
                key: value for key, value in airport.items() if key != "data"
            } | {
                "data": [
                    [
                        _convert_to_python_type(value, avoid_converting_dates) for value in lst
                    ]
                    for lst in airport["data"]
                ]
            }
            for airport in response["data"]
        ]

    # Unpack single value elements
    if unpack_single_value:
        response["data"] = [
            {
                key: value for key, value in airport.items() if key != "data"
            } | {
                "data": [lst[0] for lst in airport["data"]]
            }
            for airport in response["data"]
        ]

    return response


def accumulated_winter_season_severity_index(
    station_id: str,
    *,
    start_date: datetime | str = None,
    end_date: datetime | str = None,
    date: datetime | str = None,
    limit_by_season: bool = False
):
    """Calculates the AWSSI courtesy of MRCC (https://mrcc.purdue.edu/research/awssi) for a station.

    :param station_id: The station ID to retrieve the data from (eg. KIAD)
    :param start_date: The date to begin retrieving the data from (optional if you pass in a date).
    :param end_date: The date to stop retrieving the data from (optional if you pass in a date).
    :param date: The single day to retrieve data from (optional if you pass in a start date and end date).
    :param limit_by_season: Limits the AWSSI data calculated by its respective season as defined by MRCC."""
    station_data = get_station_data(
        station_id,
        start_date=start_date,
        end_date=end_date,
        date=date,
        elements=[ElementType.MAXIMUM_TEMPERATURE, ElementType.MINIMUM_TEMPERATURE, ElementType.SNOW, ElementType.SNOW_DEPTH],
        convert_to_their_types=True,
        replace_traces_with_integers=True
    )["data"]

    raw_awssi = [(date, calculate_awssi_index(*parameters)) + tuple(parameters) for date, *parameters in station_data]

    if limit_by_season:
        try:
            start_at = next(
                idx for idx, (date, _, maxt, __, snow, ___) in enumerate(raw_awssi)
                if maxt <= 32 or snow >= 0.1 or (date.month == 12 and date.day == 1)
            )
        except StopIteration:
            start_at = 0

        try:
            end_at = next(
                len(raw_awssi) - idx for idx, (date, _, maxt, __, snow, snow_depth) in enumerate(raw_awssi[::-1])
                if maxt <= 32 or snow >= 0.1 or snow_depth >= 1 or (date.month == 2 and date.day in {28, 29})
            )
        except StopIteration:
            end_at = len(raw_awssi)

        return [(date, awssi) for idx, (date, awssi, *_) in enumerate(raw_awssi) if start_at <= idx < end_at]
    else:
        return [(date, awssi) for date, awssi, *_ in raw_awssi]
