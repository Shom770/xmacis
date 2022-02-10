"""Finds all the -NAO events for La Nina years."""

from historical_weather import north_american_oscillation, oceanic_nino_index


ONI = oceanic_nino_index()
NAO = north_american_oscillation()

all_nina_nao_years = []

for year in range(
        max(min(ONI.keys()), min(NAO.keys())), 2021
):
    if ONI[year][1] < -0.4 and NAO[year][1] < 0:
        all_nina_nao_years.append(str(year))

print(",".join(all_nina_nao_years))
