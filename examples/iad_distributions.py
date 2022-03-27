from datetime import datetime
from operator import itemgetter
import re

from numpy import arange
import matplotlib.pyplot as plt

from historical_weather import (
    Elements,
    get_station_data,
    north_american_oscillation,
    arctic_oscillation,
    pacific_north_american_index
)

NAO = north_american_oscillation(range(1964, 2019))
AO = arctic_oscillation(range(1964, 2019))
PNA = pacific_north_american_index(range(1964, 2019))

iad_data = get_station_data(
    station_id="KIAD",
    elements=[Elements.SNOW],
    start_date=datetime(1964, 1, 1),
    end_date=datetime(2018, 12, 31)
)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

categories = ['1-2"', '3-5"', '5-8"', '8-12"', '12-18"', '18-24"', '24"+']
distributions_all = [0] * len(categories)
distributions_2 = [0] * len(categories)
distributions_1 = [0] * len(categories)
distributions_none = [0] * len(categories)

combined_storms = iad_data.combine_storms(lambda data: data.snow > .1)

X = arange(0, 35, 5)

ax.set_xticks(X, categories)
ax.set_yticks(arange(0, 101, 5))

for idx, category in enumerate(categories):
    filtered_category = [val for val in re.split('[-"\+]', category) if val]

    if len(filtered_category) == 1:
        all_storms = combined_storms.filter(lambda data: data.snow >= int(filtered_category[0]))
    else:
        low_end, high_end = map(int, filtered_category)
        all_storms = combined_storms.filter(lambda data: low_end <= data.snow < high_end)

    for storm_pd in all_storms.keys():
        if isinstance(storm_pd, tuple):
            storm_pd = storm_pd[0]

        year, month = storm_pd.year, storm_pd.month

        if NAO[year][month - 1] < 0 and AO[year][month - 1] < 0 and PNA[year][month - 1] > 0:
            distributions_all[idx] += 1
        elif (NAO[year][month - 1] < 0, AO[year][month - 1] < 0, PNA[year][month - 1] > 0).count(True) == 2:
            distributions_2[idx] += 1
        elif NAO[year][month - 1] < 0 or AO[year][month - 1] < 0 or PNA[year][month - 1] > 0:
            distributions_1[idx] += 1
        else:
            distributions_none[idx] += 1

for idx, category in enumerate(categories):
    category_distrib = sorted(
        [
            (distributions_all[idx], "y"),
            (distributions_2[idx], "g"),
            (distributions_1[idx], "r"),
            (distributions_none[idx], "b")
        ], key=itemgetter(0), reverse=True
    )
    cur_x = X[idx]
    label_mapping = {
        "y": "Had -NAO, -AO, and +PNA",
        "g": "Had two of the teleconnections listed (-NAO/-AO/+PNA)",
        "r": "Had either an -NAO, -AO, or +PNA",
        "b": "Had none of the teleconnections listed (-NAO/-AO/+PNA)"
    }
    ct_0 = sum([cat_dis.count(0) for cat_dis in category_distrib])
    highest, h_color = category_distrib[0]
    second_highest, sh_color = category_distrib[1]
    second_lowest, sl_color = category_distrib[2]
    lowest, l_color = category_distrib[3]
    if ct_0 == 0:
        ax.bar(cur_x - 1, highest, color=h_color, label=label_mapping[h_color], width=0.5)
        ax.bar(cur_x - 0.5, second_highest, color=sh_color, label=label_mapping[sh_color], width=0.5)
        ax.bar(cur_x, second_lowest, color=sl_color, label=label_mapping[sl_color], width=0.5)
        ax.bar(cur_x + 0.5, lowest, color=l_color, label=label_mapping[l_color], width=0.5)
    elif ct_0 == 1:
        ax.bar(cur_x - 0.5, highest, color=h_color, label=label_mapping[h_color], width=0.5)
        ax.bar(cur_x, second_highest, color=sh_color, label=label_mapping[sh_color], width=0.5)
        ax.bar(cur_x + 0.5, second_lowest, color=sl_color, label=label_mapping[sl_color], width=0.5)
    elif ct_0 == 2:
        ax.bar(cur_x - 0.5, highest, color=h_color, label=label_mapping[h_color], width=0.5)
        ax.bar(cur_x, second_highest, color=sh_color, label=label_mapping[sh_color], width=0.5)
    else:
        ax.bar(cur_x, highest, color=h_color, label=label_mapping[h_color], width=0.5)

ax.set_title("-NAO/-AO/+PNA Affects on Events (Washington, D.C./KIAD)")
ax.set_xlabel("Amount of Snow")
ax.set_ylabel("Amount of Events")

handles, labels = plt.gca().get_legend_handles_labels()
legend_labels = dict(zip(labels, handles))
legend_labels = {key: value for key, value in {
    'Had -NAO, -AO, and +PNA': legend_labels.get('Had -NAO, -AO, and +PNA'),
    'Had two of the teleconnections listed (-NAO/-AO/+PNA)': legend_labels.get(
        'Had two of the teleconnections listed (-NAO/-AO/+PNA)'
    ),
    'Had either an -NAO, -AO, or +PNA': legend_labels.get('Had either an -NAO, -AO, or +PNA'),
    'Had none of the teleconnections listed (-NAO/-AO/+PNA)': legend_labels.get(
        'Had none of the teleconnections listed (-NAO/-AO/+PNA)'
    )
}.items() if value}

ax.legend(legend_labels.values(), legend_labels.keys())

plt.savefig("./iad_tele.png")
