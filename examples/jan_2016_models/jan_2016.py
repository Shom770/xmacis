import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cf2cdm
import matplotlib.colors as col
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
# from ecmwfapi import ECMWFDataServer

# URL = "https://api.ecmwf.int/v1"
# KEY = "94d3ba2ccd6a320a9586bdd517219551"
# EMAIL = "shayaanwadkar@gmail.com"
# server = ECMWFDataServer(url=URL, key=KEY, email=EMAIL)
#
# server.retrieve({
#     "class": "ti",
#     "dataset": "tigge",
#     "date": "2016-01-17/to/2016-01-22",
#     "expver": "prod",
#     "grid": "0.5/0.5",
#     "levtype": "sfc",
#     "origin": "ecmf",
#     "param": "144",
#     "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144/150/156/162/168",
#     "time": "00:00:00/12:00:00",
#     "type": "fc",
#     "target": "output"
# })

# Constants
EXTENT = (-85.5, -69, 33.5, 43)
ds = xr.load_dataset("output.grib", engine="cfgrib")
cf2cdm.translate_coords(ds, cf2cdm.ECMWF)
ds["longitude"] = ds["longitude"] - 180

# Configure the plot
fig: plt.Figure = plt.figure(figsize=(12, 6))
ax: plt.Axes = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.set_extent(EXTENT)

ax.add_feature(cfeature.LAND.with_scale("50m"), zorder=25)
ax.add_feature(cfeature.OCEAN.with_scale("50m"), zorder=50)
ax.add_feature(cfeature.STATES.with_scale("50m"), lw=1.25, zorder=75)
ax.add_feature(cfeature.LAKES.with_scale("50m"), lw=1.25, zorder=75)


# Crop dataset
ds = ds.sel(latitude=slice(EXTENT[3], EXTENT[2]), longitude=slice(EXTENT[0], EXTENT[1]))
lats, lons = np.meshgrid(ds.latitude.data, ds.longitude.data)
snowfall_data = ds["sf"] / 25.4 * 10

precip_colormap = col.ListedColormap([
    '#FFFFFF','#bebebe', '#969696', '#6E6E6E', '#505050', '#96D2FA', '#78B9FA', '#50A5F5', '#3C96F5',
    '#2882F0', '#1E6EEB', '#1464D2', '#0A5AC3', '#0A5AC3', '#4D038E', '#5B038D', '#69038B',
    '#840388', '#A00485', '#C90481', '#F3047C', '#F83C9B', '#FC5EAE', '#FE6FB7', '#FB84C2',
    '#F48CC6', '#F48CC6', '#E69DCD', '#D8ADD5', '#D1B6DB', '#C3C6E0', '#B6D5F0', '#ABE2F0',
    '#A0EFF3', '#93F6F4', '#93F6F4', '#84DDDB', '#74C0C6', '#80B5CD', '#80B5CD', '#80B5CD',
    '#8BB0D3', '#8BB0D3', '#8BB0D3', '#95A9D8', '#95A9D8', '#9D9FDA', '#A4A1E0', '#A4A1E0',
    '#A4A1E0', '#AF9AE6', '#AF9AE6', '#BB90EC', '#BB90EC', '#BB90EC', '#C98AF5', '#C98AF5',
    '#C98AF5', '#C98AF5', '#C98AF5'
])
clev_precip = [0, 0.1, 0.55, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]

for idx, run_data in enumerate(snowfall_data):
    snowfall_for_run = run_data[0].data

    for step_data in run_data[1:]:
        if 21 <= int(str(step_data.valid_time.data).split("T")[0].split("-")[-1]) <= 25:
            snowfall_for_run += step_data.data

    if idx == len(snowfall_data) - 3:
        data = np.array(snowfall_for_run.data).transpose()
        data[data > 48] = 48

        C = ax.contourf(lons, lats, data, levels=clev_precip, cmap=precip_colormap, zorder=30)
        fig.colorbar(C)
        plt.show()