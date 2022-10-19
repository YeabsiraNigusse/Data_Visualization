import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline


path = 'data/eq_data_30_day_m1.json'
with open(path) as f:
    all_eq_data = json.load(f)

readabel_file = 'data/eq_data_1_day_m1.json'
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_text = [],[], [], []
for eq_dict in all_eq_dicts:
   mag = eq_dict['properties']['mag']
   lon = eq_dict['geometry']['coordinates'][0]
   lat = eq_dict['geometry']['coordinates'][1]
   title = eq_dict['properties']['title']
   mags.append(mag)
   lons.append(lon)
   lats.append(lat)
   hover_text.append(title)


data = [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'text': hover_text,
    'marker':{
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    },
    
}]
layout = Layout(title='Global Earthquakes')
fig = {'data':data, 'layout':layout}
offline.plot(fig,filename='global_earthquakes.html')