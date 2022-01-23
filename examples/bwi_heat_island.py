"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""

from datetime import datetime, timedelta
from statistics import median

from historical_weather import Elements, get_station_data
import matplotlib.pyplot as plt

dp_iad = get_station_data(
    "IAD",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2019, month=1, day=1),
    end_date=datetime.today() - timedelta(days=1)
)

dp_bwi = get_station_data(
    "BWI",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2019, month=1, day=1),
    end_date=datetime.today() - timedelta(days=1)
)


def heat_island_effects() -> tuple[float, float, float, float]:
    """Compares IAD max/min temperature to BWI's and figures out the mean/median of BWI's inaccuracies."""
    differences = {}

    for day, (iad_data, bwi_data) in zip(
            dp_iad.data_points.keys(), zip(dp_iad.data_points.values(), dp_bwi.data_points.values())
    ):
        differences[day] = (
            (bwi_data.minimum_temperature - iad_data.minimum_temperature)
            + (bwi_data.maximum_temperature - iad_data.maximum_temperature)
        ) / 2

    return differences


differences = heat_island_effects()

formatted_days = list({day.strftime("%B %Y") for day in differences.keys()})
monthly_difference = [
    sum((all_deg := [value for key, value in differences.items() if key.month == date.month])) / len(all_deg)
    for date in differences.keys() if date.day == 1
]

plt.title("BWI's difference from IAD in temperatures monthly on average since January 1st, 2019")
plt.plot(formatted_days, monthly_difference)

plt.show()