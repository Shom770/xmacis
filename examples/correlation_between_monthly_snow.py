import matplotlib.pyplot as plt
from pandas import DataFrame

from historical_weather import get_station_data, Element, ElementType, Interval, ReduceBy

station_id = "KIAD"

station_data = get_station_data(
    station_id=station_id,
    start_date="1963-01",
    end_date="por",
    elements=Element(ElementType.SNOW, interval=Interval.MONTHLY, reduce_by=ReduceBy.SUM),
    convert_to_their_types=True,
    avoid_converting_dates=True
)["data"]
data_df = DataFrame(station_data, columns=("date", "snow"))
data_df["snow"] = data_df["snow"].apply(lambda value: 0.01 if value == "T" else value)

january_snow = data_df[data_df["date"].str.contains("-01")]
february_snow = data_df[data_df["date"].str.contains("-02")]

x_data = january_snow["snow"][:-1]
y_data = february_snow["snow"]

plt.scatter(x_data, y_data, s=5, cmap="coolwarm")
plt.xlabel("January Snowfall (in.)")
plt.ylabel("Febraury Snowfall (in.)")
plt.show()