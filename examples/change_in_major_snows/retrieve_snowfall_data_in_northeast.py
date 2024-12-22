from datetime import datetime
from json import dump

from historical_weather import get_multi_station_data, Element, ElementType, Interval, ReduceBy

start_date = datetime(1950, 1, 1)
end_date = datetime(2019, 12, 31)
station_data = get_multi_station_data(
    sids=[
        "KDCA", "KBWI", "KIAD", "KPHL", "KJK", "KBOS", "KPIT", "KRIC", "KLYH", "KROA", "KORF", "KSCE",
        "KABE", "KBGM", "KSYR", "KBUF", "KROC", "KERI", "KSBY", "KALB", "KMAN", "KBDL",
        "KISP", "KBOS", "KPVD", "KORH"
    ],
    start_date=start_date,
    end_date=end_date,
    elements=Element(ElementType.SNOW, interval=Interval.DAILY, duration=3, reduce_by=ReduceBy.SUM),
    meta=["sids", "ll", "valid_daterange"],
    convert_to_their_types=True,
    avoid_converting_dates=True,
    unpack_single_value=True
)

with open("change_in_major_snows/station_output.json", "w") as file:
    dump(station_data, file, indent=2)