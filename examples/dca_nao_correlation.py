"""An analysis comparing DCA's snowstorms to where the NAO was during that time, to find a correlation."""
import datetime

from historical_weather import arctic_oscillation, Elements, get_station_data, north_american_oscillation
import matplotlib.pyplot as plt
import numpy as np


NAO = north_american_oscillation(range(1950, 2022))
AO = arctic_oscillation(range(1950, 2022))

snow_events = get_station_data(
    "KDCA",b
    [Elements.SNOW],
    start_date=datetime.datetime(year=1950, month=1, day=1),
    end_date=datetime.datetime(year=2021, month=12, day=31)
)

nao_for_events = np.array([NAO[date.year][date.month - 1] for date in snow_events.data_points])
total_snow = np.array([snow_info.snow for snow_info in snow_events.data_points.values()])

dc_in_snow = plt.imread("./examples/dc_in_snow.jpg")

fig, ax = plt.subplots()

dc_in_snow = ax.imshow(
    dc_in_snow,
    alpha=0.3,
    extent=[total_snow.min(), total_snow.max(), nao_for_events.min(), nao_for_events.max()]
)

plt.title("Total Snow for DCA vs. NAO during that time")
plt.xlabel("Total Snow Monthly (in.)")
plt.ylabel("NAO Index During the Event Plotted")

ax.scatter(total_snow, nao_for_events, c=nao_for_events, cmap="plasma")

ax.plot(
    total_snow,
    np.poly1d(np.polyfit(total_snow, nao_for_events, 1))(total_snow),
    "r--",
    lw=1
)

plt.show()
