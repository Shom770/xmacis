from json import load

import cartopy.crs as ccrs
import cartopy.feature as cfeature

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np
from matplotlib.offsetbox import AnchoredText

# Load and parse data
with open("trend_in_snowfall.json") as file:
    raw_data = load(file)
    lons = [airport[0][0] for airport in raw_data.values()]
    lats = [airport[0][1] for airport in raw_data.values()]
    correlations = [airport[1] for airport in raw_data.values()]

extent = (-83, -69.5, 36, 44)

fig: plt.Figure = plt.figure(figsize=(12, 6))
ax: plt.Axes = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.set_extent(extent)

ax.add_feature(cfeature.LAND.with_scale("50m"), zorder=25)
ax.add_feature(cfeature.OCEAN.with_scale("50m"), zorder=50)
ax.add_feature(cfeature.STATES.with_scale("50m"), lw=1.25, zorder=75)
ax.add_feature(cfeature.LAKES.with_scale("50m"), lw=1.25, zorder=75)

levels = np.arange(-1, 1.1, 0.1)

cmap = cm.get_cmap("coolwarm_r")
norm = colors.BoundaryNorm(levels, cmap.N)

C = ax.scatter(
    lons, lats, s=75, c=correlations, edgecolors="black",
    cmap=cmap, norm=norm, transform=ccrs.PlateCarree(), zorder=100
)
fig.colorbar(
    C,
    label="Correlation Coefficient",
    aspect=3.175
)
plt.suptitle(
    f"Trend in the Largest Snow Events by Decade",
    fontsize=14,
    ha="left",
    x=0.1225,
    y=0.94,
    fontweight="bold"
)
plt.title(
    f"Uses data between 1950 and 2023 across {len(correlations)} airports in the Northeast, Made by @AtlanticWx",
    fontsize=10,
    loc="left"
)
ax.add_artist(
    AnchoredText(
        "Made by @AtlanticWx",
        loc="lower right",
        prop={"size": 10},
        frameon=True
    )
)
plt.show()
