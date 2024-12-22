from datetime import datetime, timedelta
from functools import reduce
import numpy as np
from historical_weather import Element, ElementType, get_multi_station_data


def chunked(lst: list, n: int) -> list:
    new_list = [[]]

    for idx, value in enumerate(lst):
        new_list[-1].append(value)

        if idx + 1 == n:
            new_list.append([])

    return new_list


east_sids = ["KIAD", "KBWI"]
west_sids = ["KCVG", "KDAY"]
start_date = datetime(1980, 1, 1)
end_date = datetime(2023, 6, 1)


appalachia_east, appalachia_west = chunked(
    get_multi_station_data(
        sids=east_sids + west_sids,
        start_date=start_date,
        end_date=end_date,
        elements=[ElementType.SNOW, ElementType.AVERAGE_TEMPERATURE],
        convert_to_their_types=True,
        avoid_converting_dates=True
    )["data"],
    len(east_sids)
)

raw_values_east = [
    np.array([[value if value != 'T' else 0.01 for value in lst] for lst in airport]).transpose()
    for airport in appalachia_east
]
raw_values_west = [
    np.array([[value if value != 'T' else 0.01 for value in lst] for lst in airport]).transpose()
    for airport in appalachia_west
]
appalachia_east_snow, appalachia_east_temps = reduce(np.ndarray.__add__, raw_values_east) / len(east_sids)
appalachia_west_snow, appalachia_west_temps = reduce(np.ndarray.__add__, raw_values_west) / len(west_sids)

temperature_difference = np.nanmean(temperature_difference := appalachia_east_temps - appalachia_west_temps)
days_with_more_snow_west = appalachia_west_snow[appalachia_west_snow > appalachia_east_snow]

flakes_missed_out_on = days_with_more_snow_west[days_with_more_snow_west < 0.1]
events_missed_out = []
events_gained = []

for (east_snow, east_temps, west_snow, west_temps) in zip(
    appalachia_east_snow, appalachia_east_temps, appalachia_west_snow, appalachia_west_temps
):
    if (
        west_snow > 0.1   # Real snow events
        and west_snow > east_snow   # More snow west
        and east_temps <= 33 and west_temps <= 33  # Don't include cutters, the mountains don't affect it.
    ):
        events_missed_out.append(west_snow - east_snow)

    if east_temps <= 33 and west_temps > 32 and east_snow > west_snow:  # CAD
        events_gained.append(east_snow - west_snow)

else:
    events_missed_out = np.array(events_missed_out)
    events_gained = np.array(events_gained)

events_missed_out_per_year = len(events_missed_out) / (end_date.year - start_date.year)
events_gained_per_year = len(events_gained) / (end_date.year - start_date.year)

snow_missed_on_per_year = events_missed_out.sum() / (end_date.year - start_date.year)
snow_gained_per_year = events_gained.sum() / (end_date.year - start_date.year)

print(f"On average, temperatures would be {temperature_difference.mean():.1f} degrees warmer.")
print(f"On average, we'd gain {events_missed_out_per_year:.1f} snow events a year and lose {events_gained_per_year:.1f} snow events a year.")
print(f"On average, we'd get {snow_missed_on_per_year:.1f} inches more snow in a season and {snow_gained_per_year:.1f5..5} inches less snow in a season.")