"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""

from datetime import datetime

from historical_weather import Elements, get_station_data

dp_iad = get_station_data(
    "IAD",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2020, month=2, day=20),  # The start date is Feb. 20th, 2020 because that is when BWI became a 'heat island' apparently.
    end_date=datetime.today()
)

dp_bwi = get_station_data(
    "BWI",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2020, month=2, day=20),
    end_date=datetime.today()
)
