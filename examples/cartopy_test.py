from dataclasses import dataclass
from datetime import datetime, timedelta
from itertools import chain

from cartopy import feature as cfeature
from matplotlib.animation import FuncAnimation

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import requests


@dataclass(repr=True)
class SnowSquallWarning:
    start_time: datetime
    end_time: datetime
    geometry_lat: list
    geometry_long: list


def flatten(list_to_flatten: list, *, times: int = 1):
    for _ in range(times):
        list_to_flatten = list(chain.from_iterable(list_to_flatten))

    return list_to_flatten


snow_squall_warnings = requests.get(
    url=(
        "https://mesonet.agron.iastate.edu/api/1/vtec/sbw_interval.geojson?"
        "begints=2022-02-18T00:00&endts=2022-02-20T00:00&ph=SQ&only_new=false"
    )
).json()

all_sqws = []

for sqw in snow_squall_warnings["features"]:
    coordinates = flatten(sqw["geometry"]["coordinates"], times=2)
    snow_squall_warning = SnowSquallWarning(
        start_time=datetime.fromisoformat(sqw["properties"]["utc_polygon_begin"][:-1]),
        end_time=datetime.fromisoformat(sqw["properties"]["utc_polygon_end"][:-1]),
        geometry_lat=[coordinate[1] for coordinate in coordinates],
        geometry_long=[coordinate[0] for coordinate in coordinates]
    )
    all_sqws.append(snow_squall_warning)

extent = (-93.7, -66.6, 36.6, 47.5)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=np.mean(extent[:2])))
ax.set_extent(extent)

ax.add_feature(cfeature.LAND.with_scale("50m"))
ax.add_feature(cfeature.OCEAN.with_scale("50m"))
ax.add_feature(cfeature.COASTLINE.with_scale("50m"))
ax.add_feature(cfeature.LAKES.with_scale("50m"), alpha=0.5)
ax.add_feature(cfeature.STATES.with_scale("50m"))

lines = []


def frame_gen():
    for sqw_time in sorted({sqw.start_time for sqw in all_sqws}):
        yield sqw_time


def animate(frame):
    for poly in flatten(lines):
        poly.set_visible(False)

    for current_sqw in all_sqws:
        if current_sqw.start_time <= frame <= current_sqw.end_time:
            lines.append(ax.fill(
                current_sqw.geometry_long,
                current_sqw.geometry_lat,
                color="#c71585",
                alpha=0.5,
                edgecolor="black",
                lw=2,
                transform=ccrs.PlateCarree()
            ))

    est_time = frame - timedelta(hours=5)
    lines.append([ax.text(
        -93.4, 47.4,
        (
            f"February {est_time.day}th, {frame.year}"
            f" - {est_time.hour - 12 if est_time.hour > 12 else est_time.hour}"
            f":{str(est_time.minute).zfill(2)} {'A.M' if est_time.hour < 12 else 'P.M'} EST"
        ),
        size=16,
        transform=ccrs.PlateCarree(),
        bbox=dict(facecolor='sandybrown', boxstyle='round')
    )])

    return flatten(lines)


animation = FuncAnimation(fig, animate, frames=frame_gen, blit=False)
animation.save('./animation_sqw.gif', fps=10)
