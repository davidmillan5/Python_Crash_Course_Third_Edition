from pathlib import Path
import json

import plotly.express as px

# read data as a string and convert to Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)


# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))

mags, lons, lats, eq_titles = [], [], [], []
[mags.append(eq['properties']['mag']) or lons.append(eq['geometry']['coordinates'][0]) or lats.append(eq['geometry']['coordinates'][1]) or eq_titles.append(eq['properties']['title']) for eq in all_eq_dicts]


title = 'Global Earthquakes'
fig = px.scatter_geo(lat = lats, lon = lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()