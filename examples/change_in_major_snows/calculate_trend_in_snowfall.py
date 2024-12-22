from collections import defaultdict
from datetime import datetime
from json import dump, load

import numpy as np
import pandas as pd

with open("change_in_major_snows/station_output.json") as file:
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2019, 12, 31)
    raw_data = load(file)
    pearson_coefficients = {}

for airport in raw_data["data"]:
    snowfall_data = pd.DataFrame(
        {
            "date": pd.date_range(start_date, end_date, freq="1D", inclusive="both").values,
            "snow": [day if day != "T" else 0.01 for day in airport["data"]]
        }
    )
    maximum_snowfall_by_year = defaultdict(int)

    for year in range(start_date.year, 2020):
        snow_in_year = snowfall_data[snowfall_data["date"].dt.strftime('%Y-%m-%d').str.startswith(str(year))]
        snow_in_year = snow_in_year[snow_in_year["snow"].notnull()]
        maximum_snowfall = snow_in_year["snow"].max()

        if pd.notna(maximum_snowfall) and maximum_snowfall > maximum_snowfall_by_year[year - year % 10]:
            maximum_snowfall_by_year[year - year % 10] = maximum_snowfall

    # Plotting
    maximum_snowfall_by_year = {key: value for key, value in maximum_snowfall_by_year.items() if value != 0}
    years = maximum_snowfall_by_year.keys()
    snowfall = maximum_snowfall_by_year.values()
    pearson_r = np.corrcoef(np.array([int(year) for year in years]), np.array(list(snowfall)))[0, 1]
    pearson_coefficients[
        next(stripped_sid for sid in airport["meta"]["sids"] if not (stripped_sid := sid.split()[0]).isnumeric())
    ] = (airport["meta"]["ll"], pearson_r)

with open("change_in_major_snows/trend_in_snowfall.json", "w") as file:
    dump(pearson_coefficients, file, indent=2)
