"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""
from collections import defaultdict
from datetime import datetime, timedelta

from historical_weather import Elements, get_station_data
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


dp_iad = get_station_data(
    "IAD",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2016, month=1, day=1),
    end_date=datetime.today() - timedelta(days=1)
)

dp_bwi = get_station_data(
    "BWI",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2016, month=1, day=1),
    end_date=datetime.today() - timedelta(days=1)
)


def heat_island_effects() -> dict:
    """Compares IAD max/min temperature to BWI's and figures out the mean/median of BWI's inaccuracies."""
    differences = defaultdict(list)

    for day, (iad_data, bwi_data) in zip(
            dp_iad.data_points.keys(), zip(dp_iad.data_points.values(), dp_bwi.data_points.values())
    ):
        differences[day.strftime("%B %Y")].append((
            (bwi_data.minimum_temperature - iad_data.minimum_temperature)
            + (bwi_data.maximum_temperature - iad_data.maximum_temperature)
        ) / 2)

    return {key: sum(value) / len(value) for key, value in differences.items()}


differences = heat_island_effects()

plt.title("BWI's difference from IAD in temperatures monthly on average since January 1st, 2016")

plt.xticks([tick for tick in range(len(differences.keys()))], differences.keys(), rotation=90)
plt.axvline(x=48)  # location of the x value "Jan 2020", i.e. when BWI became a heat island.
plt.axhline(y=0)  # demonstrate how no month average has reached below IAD on average

plt.plot(differences.keys(), differences.values(), color="red")

plt.show()