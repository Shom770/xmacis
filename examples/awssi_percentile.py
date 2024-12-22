from datetime import datetime, timedelta

import matplotlib.pyplot as plt
from matplotlib import cm
from numpy import arange, logical_and
from pandas import DataFrame, date_range

from historical_weather import accumulated_winter_season_severity_index

station_id = "KEWR"
awssi_data = DataFrame(
    accumulated_winter_season_severity_index(
        station_id,
        start_date="por",
        end_date="por",
    ),
    columns=("date", "points")
)
start_date = awssi_data["date"].iloc[0]
awssi_by_periods = []

for period in date_range(start_date, datetime.today(), freq="1D"):
    if period.month not in {11, 12, 1, 2, 3}:
        continue

    filtered_data = awssi_data[
        logical_and(period <= awssi_data["date"], awssi_data["date"] <= period + timedelta(days=7))
    ]
    if (total_points := filtered_data["points"].sum()) > 0:
        awssi_by_periods.append((period, total_points))
else:
    awssi_by_periods = DataFrame(awssi_by_periods, columns=("date", "points"))

# Calculate percentile of AWSSI value
starting_date_to_compare = datetime(1991, 6, 1)
distribution_of_snow = awssi_by_periods[awssi_by_periods["date"] >= starting_date_to_compare]
period_starts_at = datetime(2021, 1, 30)
awssi_points_to_use = awssi_by_periods[
    logical_and(
        period_starts_at <= awssi_by_periods["date"],
        awssi_by_periods["date"] <= period_starts_at + timedelta(days=7)
    )
]["points"].max()

plt.style.use("ggplot")

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

n, bins, patches = ax.hist(distribution_of_snow[distribution_of_snow["date"] < period_starts_at]["points"], bins=arange(1, awssi_by_periods["points"].max(), 1))

# Copy and pasted from stackoverflow to use a colormap
cm = cm.get_cmap("RdYlBu_r")
for i, p in enumerate(patches):
    plt.setp(p, "facecolor", cm(0.95 - i / len(patches) * 5))
    plt.setp(p, "alpha", 0.6 + i / 20 if 0.5 + i / 10 <= 1 else 1)

ax.set_yticks([])

plt.xlabel("Accumulated Winter Season Severity Index (Courtesy of MRCC)")
plt.ylabel("Weeks")

plt.suptitle(
    f"\"Wintry\" Weeks since {starting_date_to_compare.strftime('%B %Y')} at {station_id}",
    fontsize=14,
    ha="left",
    x=0.1225,
    y=0.92,
    fontweight="bold"
)
plt.title(
    f"Histogram of weeks and their Accumulated Winter Season Severity Index (more is colder & snowier), Made by @AtlanticWx",
    fontsize=10,
    loc="left"
)

ax.axvline(x=awssi_points_to_use + 0.5, color=cm(0))
plt.text(x=awssi_points_to_use - 1.5, y=ax.get_ylim()[1] / 2 - 5, s="Last Week", fontsize=10, fontweight="bold", rotation=90)
plt.show()
