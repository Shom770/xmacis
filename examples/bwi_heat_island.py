"""An analysis comparing daily temperatures between IAD and BWI to see the effect of BWI's 'heat island'."""

from datetime import datetime, timedelta
from statistics import median

from historical_weather import Elements, get_station_data

dp_iad = get_station_data(
    "IAD",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2020, month=2, day=20),
    # The start date is Feb. 20th, 2020 because that is when BWI became a 'heat island' apparently.
    end_date=datetime.today() - timedelta(days=1)
)

dp_bwi = get_station_data(
    "BWI",
    [Elements.MINIMUM_TEMPERATURE, Elements.MAXIMUM_TEMPERATURE],
    start_date=datetime(year=2020, month=2, day=20),
    end_date=datetime.today() - timedelta(days=1)
)


def heat_island_effects() -> tuple[float, float, float, float]:
    """Compares IAD max/min temperature to BWI's and figures out the mean/median of BWI's inaccuracies."""
    relative_heat = []
    hotter_on_avg = []

    for day, (iad_data, bwi_data) in zip(
            dp_iad.data_points.keys(), zip(dp_iad.data_points.values(), dp_bwi.data_points.values())
    ):
        relative_heat.append((
                                     (bwi_data.minimum_temperature / iad_data.minimum_temperature)
                                     + (bwi_data.maximum_temperature / iad_data.maximum_temperature)
                             ) / 2)
        hotter_on_avg.append((
                                     (bwi_data.minimum_temperature - iad_data.minimum_temperature)
                                     + (bwi_data.maximum_temperature - iad_data.maximum_temperature)
                             ) / 2)

    return (
        sum(relative_heat) / len(relative_heat),
        median(relative_heat),
        sum(hotter_on_avg) / len(hotter_on_avg),
        median(hotter_on_avg)
    )


mean_relative, median_relative, mean_absolute, median_absolute = heat_island_effects()


