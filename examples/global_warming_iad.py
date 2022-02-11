"""An analysis comparing IAD's average monthly high temperature during summer from 1950 to now."""
from collections import defaultdict
from datetime import datetime, timedelta

from historical_weather import Elements, get_station_data
import matplotlib.pyplot as plt
import numpy as np

dp_iad = get_station_data(
    "IAD",
    [Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=1950, month=1, day=1),
    end_date=datetime.today() - timedelta(days=1)
)


def global_warming_effects() -> dict:
    """Gets IAD's average monthly high temperature from 1950 till now."""
    years_and_avg = defaultdict(list)

    for period, data in dp_iad.data_points.items():
        if not datetime(year=period.year, month=6, day=22) <= period < datetime(year=period.year, month=9, day=23):
            continue

        years_and_avg[period.year].append(data.maximum_temperature)

    return {key: sum(value) / len(value) for key, value in years_and_avg.items()}


global_warming_iad = global_warming_effects()

years = np.array(global_warming_iad.keys())
avg_high = np.array(global_warming_iad.values())

plt.scatter(years, avg_high)

plt.plot(
    years,
    np.poly1d(np.polyfit(years, avg_high, 1))(years),
    "r--",
    lw=1
)
