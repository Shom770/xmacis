import matplotlib.pyplot as plt
import pandas as pd
from historical_weather import Element, ElementType, Normal, get_station_data

station_id = "KILM"
station_data = get_station_data(
    station_id,
    start_date="1981-01-01",
    end_date="2010-01-01",
    elements=[
        Element(ElementType.SNOW),
        Element(ElementType.MINIMUM_TEMPERATURE),
        Element(ElementType.MINIMUM_TEMPERATURE, normal=Normal.FROM_1981),
        Element(ElementType.MINIMUM_TEMPERATURE, normal=Normal.FROM_1991),
        Element(ElementType.MAXIMUM_TEMPERATURE),
        Element(ElementType.MAXIMUM_TEMPERATURE, normal=Normal.FROM_1981),
        Element(ElementType.MAXIMUM_TEMPERATURE, normal=Normal.FROM_1991),
    ],
    convert_to_their_types=True,
    avoid_converting_dates=True
)

snow_dataframe = pd.DataFrame(
    station_data["data"],
    columns=("date", "snow", "low", "low_1981", "low_1991", "high", "high_1981", "high_1991")
).map(lambda value: 0.01 if value == 'T' else value)
days_with_snow = snow_dataframe[snow_dataframe["snow"] > 0].reset_index(drop=True)
snow_events_lost = {}

for _, (date, snow, low, low_1981, low_1991, high, high_1981, high_1991) in days_with_snow.iterrows():
    low_departure = low - low_1981
    high_departure = high - high_1981
    new_low = low_1991 + low_departure
    new_high = high_1991 + high_departure

    if (new_low + new_high) / 2 >= 33 and new_low > 32 and new_low != low:
        snow_events_lost[date] = (snow, new_low, new_high, low, high)

snow_events_lost = sorted(snow_events_lost.items(), key=lambda pair: pair[1][0], reverse=True)
events_lost = []

for place, (day, (st, nl, nh, ol, oh)) in enumerate(snow_events_lost, start=1):
    if st < 0.1:
        continue
    print(f"{place}. {day} with {st}\" of snow. The new low would be {nl} deg versus {ol} deg and the new high would be {nh} deg versus {oh} deg")
    events_lost.append(st)

plt.suptitle(
    f"Snow Events Lost at {station_data['meta']['name'].split()[0].lower().title()} "
    f"(1981-2010)", fontweight="bold", ha="left", fontsize=12, x=0.125, y=0.955
)
plt.title(f"Made by @AtlanticWx, Data from {station_id.replace('K', '')}", fontsize=8, ha="left", x=0)
n, bins, patches = plt.hist(events_lost, rwidth=0.9)
plt.xlabel("Snow from Event (in.)")
plt.ylabel("# of Events Lost")

# Change color of histograms
bin_centers = 0.5 * (bins[:-1] + bins[1:])
cm = plt.cm.get_cmap("Reds")

col = bin_centers - min(bin_centers)
col /= max(col)

for c, p in zip(col, patches):
    plt.setp(p, "facecolor", cm(c + 0.25))

plt.show()

