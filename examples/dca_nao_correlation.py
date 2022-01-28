"""An analysis comparing DCA's snowstorms to where the NAO was during that time, to find a correlation."""
import datetime

from historical_weather import Elements, get_station_data, north_american_oscillation
import matplotlib.pyplot as plt
import numpy as np


NAO = north_american_oscillation(range(1950, 2022))

snow_events = get_station_data(
    "KJFK",
    [Elements.SNOW],
    start_date=datetime.datetime(year=1950, month=1, day=1),
    end_date=datetime.datetime(year=2021, month=12, day=31)
).filter(lambda data: data.snow >= 3)

nao_for_events = np.array([NAO[date.year][date.month - 1] for date in snow_events.data_points])
total_snow = np.array([snow_info.snow for snow_info in snow_events.data_points.values()])

plt.title("Total Snow for DCA vs. NAO during that time")
plt.scatter(total_snow, nao_for_events, c=nao_for_events, cmap="plasma")

plt.show()