import pandas as pd
import plotly.graph_objects as go

# Import data from CSV file, we apply a filter for only gather information from specific columns
data = pd.read_csv("/home/luis/proyectos/python/python_exercises/resources/inegi2010/conjunto_de_datos/iter_00_cpv2010.csv",
                   usecols=["nom_ent", "entidad", "mun", "loc", "ocupvivpar","prom_ocup","pro_ocup_c","vph_pisodt","vph_pisoti","vph_1dor","vph_2ymasd","vph_1cuart","vph_2cuart","vph_3ymasc"],
                   sep=",",
                   encoding="utf-8")

# We rename some columns name to became them more friendly
data = data.rename(columns={'entidad': 'id'})

# We are gonna handle stats per state, we will omit municipalities and neighborhoods
data = data.loc[(data['id'] > 0) & (data['mun'] == 0) & (data['loc'] == 0)]

# Initialize figure
fig = go.Figure()

# Initialize empty arrays
states = []
population = []

# Fill in empty arrays.
for index, obj in data.iterrows():
     states.append(obj['nom_ent'])
     population.append(pd.to_numeric(obj['vph_3ymasc'], errors='coerce'))

# Plot the dataframe

fig.add_trace(go.Bar(x=states,
                     y=population,
                     name='Rest of world',
                     marker_color='rgb(55, 83, 109)'
              ))

fig.update_layout(
    title='Viviendas con 3 cuartos o más (INEGI)',
    xaxis_tickfont_size=12,
    yaxis=dict(
        title='Viviendas',
        titlefont_size=16,
        tickfont_size=12,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    xaxis_tickangle=-90
)
fig.show()