from ast import literal_eval
from datetime import datetime

import typing

import requests


_SESSION = requests.Session()


class DataPoints:
    """Contains all the data recieved from the xmacis API from one request."""

    def __init__(self, data_points: dict):
        self.data_points = data_points

    def filter(
            self,
            condition: typing.Callable,
            within: typing.Optional[int] = None,
            min_periods: typing.Optional = None
    ) -> "DataPoints":
        """Filter through each data point in `self.data_points` with the condition provided (callable)"""

        filtered = {period: data for period, data in self.data_points.items() if condition(data)}

        if not within:
            return DataPoints(filtered)
        else:
            all_periods = []
            data_points = {}
            difference_between_periods = 0

            periods_meeting_condition = list(filtered.keys())

            for idx, (period, data) in enumerate(filtered.items()):
                # Skip the first period
                if idx == 0:
                    continue

                previous_period = periods_meeting_condition[idx - 1]

                # Ensure that the difference between two periods are within the range (within)
                if (period - previous_period).total_seconds() // 86400 + difference_between_periods <= within:
                    if previous_period not in data_points:
                        data_points[previous_period] = filtered[previous_period]

                    data_points[period] = data
                else:
                    # If data_points isn't empty and the range has been exceeded, add it to the list of periods
                    if data_points:
                        all_periods.append(DataPoints(data_points))
                        data_points = {}

                    difference_between_periods = 0
            else:
                # If the last period sufficed for the conditions, add it to the periods list
                if data_points:
                    all_periods.append(DataPoints(data_points))

            if min_periods:
                return [period for period in all_periods if len(period.data_points.keys()) >= min_periods]
            else:
                return all_periods

    def __repr__(self):
        return f"DataPoints({self.data_points})"


class _Data:
    """Contains the data retrieved from the xmacis API for a single point in time."""

    def __init__(self, **kwargs):
        for element, value in kwargs.items():
            if value != "T" and value != "M":
                setattr(self, element.lower(), literal_eval(value))
            else:
                setattr(self, element.lower(), 0.01 if value == "T" else 0.1)

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
) -> DataPoints:
    """Retrieves the station data based off the filters provided."""
    parameters = {param_name: param_value.strftime("%Y-%m-%d") if isinstance(param_value, datetime) else param_value
                  for param_name, param_value in zip(
        ("sid", "sdate", "edate", "date", "elems"),
        (station_id, start_date, end_date, date, ",".join(element.value for element in elements))
    ) if param_value}

    response = _SESSION.get("http://data.rcc-acis.org/StnData", params=parameters).json()

    data_points = {}

    for point in response["data"]:
        data_points[datetime.strptime(point[0], "%Y-%m-%d")] = _Data(
            **{element._name_: value for element, value in zip(elements, point[1:])}
        )

    return DataPoints(data_points)


from elements import Elements
dp = get_station_data("DCA", [Elements.SNOW], start_date=datetime(1950, 1, 1), end_date=datetime.today())

lst = dp.filter(lambda data: data.snow >= 2.6, within=13, min_periods=3)

print("[\n\t",end="")
print(*lst, sep="\n\t")
print("]")