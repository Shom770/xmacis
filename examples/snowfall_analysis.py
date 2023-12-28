from historical_weather import Element, ElementType, Interval, Normal, ReduceBy, get_station_data

print(get_station_data(
    "KIAD",
    start_date="1991-01-01",
    end_date="2023-01-01",
    elements=[
        Element(ElementType.SNOW, interval=Interval.DAILY, duration=3, reduce_by=ReduceBy.SUM),
        Element(ElementType.MINIMUM_TEMPERATURE, interval=Interval.DAILY, duration=3, reduce_by=ReduceBy.MINIMUM)
    ],
    convert_to_their_types=True
))