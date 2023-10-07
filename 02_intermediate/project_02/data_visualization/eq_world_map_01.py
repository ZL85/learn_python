import plotly.express as px
from pathlib import Path
import json

path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data["features"]

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    title = eq_dict["properties"]["title"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

fig = px.scatter(
    x=lons,
    y=lats,
    labels={"x": "经度", "y": "纬度"},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
)

out_path = Path("htmls/eq_world_map_01.html")
fig.write_html(out_path)
fig.show()
