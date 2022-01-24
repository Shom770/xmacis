"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""
from collections import defaultdict
from datetime import datetime, timedelta

from historical_weather import Elements, get_station_data
import matplotlib.pyplot as plt

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


def heat_island_effects() -> tuple[dict, dict]:
    """Compares IAD's monthly avg. high temperature to BWI's to see the effects of the heat island at BWI."""
    average_bwi_high = defaultdict(list)
    average_iad_high = defaultdict(list)

    for day, (iad_data, bwi_data) in zip(
            dp_iad.data_points.keys(), zip(dp_iad.data_points.values(), dp_bwi.data_points.values())
    ):
        average_bwi_high[day.strftime("%B %Y")].append(bwi_data.maximum_temperature)
        average_iad_high[day.strftime("%B %Y")].append(iad_data.maximum_temperature)

    return (
        {key: sum(value) / len(value) for key, value in average_bwi_high.items()},
        {key: sum(value) / len(value) for key, value in average_iad_high.items()}
    )


avg_bwi_high, avg_iad_high = heat_island_effects()

plt.title("BWI and IAD's monthly average high temperature since January 1st, 2016")

plt.xticks([tick for tick in range(len(avg_bwi_high.keys()))], avg_bwi_high.keys(), rotation=90)

plt.plot(avg_bwi_high.keys(), avg_bwi_high.values(), color="red")
plt.plot(avg_iad_high.keys(), avg_iad_high.values(), color="blue")

plt.show()