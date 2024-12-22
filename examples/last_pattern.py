from datetime import datetime

from pandas import DataFrame

from historical_weather import get_station_data, Element, ElementType, Interval, ReduceBy

BWI_SNOWFALL = (4.2, 4.1 + 0.8)
DCA_SNOWFALL = (3.7, 3.4 + 0.7)
IAD_SNOWFALL = (5.1, 4.1 + 0.3)
print(sum(DCA_SNOWFALL), sum(IAD_SNOWFALL), sum(BWI_SNOWFALL))
data = []

for sid in ("KDCA", "KBWI", "KIAD"):
    station_data = get_station_data(
        station_id=sid,
        start_date="1963-01-01",
        end_date="2024-01-01",
        elements=Element(ElementType.SNOW, interval=Interval.DAILY, duration=3, reduce_by=ReduceBy.SUM),
        convert_to_their_types=True
    )["data"]
    filtered_data = []
    dates = set()
    data_iter = iter(zip(station_data, station_data[1:], station_data[2:]))

    for (date1, day1), (date2, day2), (date3, day3) in data_iter:
        if (
            day1 != "T" and day2 != "T" and day3 != "T"
            and day1 > 0 and day2 > 0 and day3 > 0
        ):
            date_chosen, snow_chosen = max((date1, day1), (date2, day2), (date3, day3), key=lambda pair: pair[1])

            if date_chosen not in dates:
                filtered_data.append((date_chosen, snow_chosen))
                dates.add(date_chosen)

    df = DataFrame(filtered_data, columns=("date", "snow"))
    data.append(df)

weekly_dfs = []

for station in data:
    weekly_data = []
    previous_date = datetime(1950, 1, 1)
    accumulator = []

    for _, (date, snow) in station.iterrows():
        if (date - previous_date).days <= 7:
            accumulator.append((date, snow))
        else:
            if accumulator:
                snow_events = [pair[-1] for pair in accumulator]
                weekly_data.append((previous_date, snow_events, len(snow_events)))

            previous_date = date
            accumulator = [(date, snow)]

    weekly_df = DataFrame(weekly_data, columns=("date", "events", "num"))
    weekly_dfs.append(weekly_df[weekly_df["num"] > 1])

dca_data, bwi_data, iad_data = weekly_dfs
print(dca_data)