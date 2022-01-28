"""An analysis comparing DCA's snowstorms to where the NAO was during that time, to find a correlation."""
import datetime

from historical_weather import Elements, get_station_data, north_american_oscillation
import matplotlib.pyplot as plt

NAO = north_american_oscillation(range(1950, 2022))
snow_events = get_station_data(
    "KDCA",
    [Elements.SNOW],
    start_date=datetime.datetime(year=1950, month=1, day=1),
    end_date=datetime.datetime.today()
).filter(lambda data: data.snow >= 2)

nao_for_events = []
total_snow = []

for date, dca_snow in dict(snow_events).items():
    nao_for_events.append(NAO[date.year][date.month - 1])
    total_snow.append(dca_snow.snow)

plt.title("Total Snow vs. NAO during that time")
plt.scatter(total_snow, nao_for_events)

plt.show()