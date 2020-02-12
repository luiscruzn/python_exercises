import pandas as pd
import plotly.express as px
from urllib.request import urlopen
import json
with urlopen("file:////home/luis/proyectos/python/python_exercises/resources/estados-de-mexico.geojson") as response:
    counties = json.load(response)

# Import data from CSV file, we apply a filter for only gather information from specific columns
data = pd.read_csv("/home/luis/proyectos/python/python_exercises/resources/inegi2010/conjunto_de_datos/iter_00_cpv2010.csv",
                   usecols=["nom_ent", "entidad", "mun", "loc", "p_60ymas"],
                   sep=",",
                   encoding="utf-8")

# We rename some columns name to became them more friendly
data = data.rename(columns={'entidad': 'id', 'p_60ymas': 'population'})

# We are gonna handle stats per state, we will omit municipalities and neighborhoods
data = data.loc[(data['id'] > 0) & (data['mun'] == 0) & (data['loc'] == 0)]

# We homologate "id" with the INEGI id in GEOJSON map
data["id"] = "MX" + data["id"].map('{:0>2}'.format)

# "We convert field type from string to numeric in order to show a heat map"
data['population'] = pd.to_numeric(data['population'], errors='coerce')

# Plot the map using "curated" dataframe
fig = px.choropleth_mapbox(data, geojson=counties,
                           color="population",
                           #hover_name="nom_ent",
                           #hover_data=["population"],
                           locations="id",
                           featureidkey="properties.codigo",
                           center={"lat": 22.7684307, "lon": -102.5814133},
                           mapbox_style="carto-positron",
                           color_continuous_scale=["white", "red"],
                           zoom=5)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()