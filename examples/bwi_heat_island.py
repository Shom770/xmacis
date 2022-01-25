"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""
from collections import defaultdict
from datetime import datetime, timedelta

from historical_weather import Elements, get_station_data
import matplotlib.dates as dates
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
    "DCA",
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

departure = np.array(list(differences.values()))
month_labels = np.array(list(differences.keys()))

plt.title("DCA's difference from IAD in temperatures monthly on average since January 1st, 2016")

plt.xticks([tick for tick in range(len(month_labels))], month_labels, rotation=90)

plt.axvline(x=48)  # since BWI became a 'heat island'
plt.axhline(y=0)  # demonstrate how no month average has reached below IAD on average

plt.plot(month_labels, departure, color="red")

plt.show()
