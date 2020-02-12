import pandas as pd
import plotly.express as px

# Import data from CSV file, we apply a filter for only gather information from specific columns
data = pd.read_csv("/home/luis/proyectos/python/python_exercises/resources/inegi2010/conjunto_de_datos/iter_00_cpv2010.csv",
                   usecols=["nom_ent", "entidad", "mun", "loc", "ocupvivpar", "vph_pisodt","vph_pisoti","vph_1dor","vph_2ymasd","vph_1cuart","vph_2cuart","vph_3ymasc"],
                   sep=",",
                   encoding="utf-8")

# We rename some columns name to became them more friendly
data = data.rename(columns={'entidad': 'id'})

# We are gonna handle stats per state, we will omit municipalities and neighborhoods
data = data.loc[(data['id'] > 0) & (data['mun'] == 0) & (data['loc'] == 0)]

# Initialize an empty dataframe, in which we will store "tidy data"
DF1 = pd.DataFrame(columns=['Entidad', 'Tipo_Vivienda', 'population'])
for index, obj in data.iterrows():
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': 'Ocupantes', 'population':  pd.to_numeric(obj['ocupvivpar'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': 'Piso dif tierra', 'population': pd.to_numeric(obj['vph_pisodt'], errors='coerce')},  ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': 'Piso de tierra', 'population': pd.to_numeric(obj['vph_pisoti'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': '1 dormitorio', 'population': pd.to_numeric(obj['vph_1dor'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': '2 o más dorm.', 'population': pd.to_numeric(obj['vph_2ymasd'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': '1 cuarto', 'population': pd.to_numeric(obj['vph_1cuart'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': '2 cuartos', 'population': pd.to_numeric(obj['vph_2cuart'], errors='coerce')}, ignore_index=True)
    DF1 = DF1.append({'Entidad': obj['nom_ent'], 'Tipo_Vivienda': '3 o más cuartos', 'population': pd.to_numeric(obj['vph_3ymasc'], errors='coerce')}, ignore_index=True)

# Replace NaN with 0
DF1.fillna(0, inplace=True)

# Plot dataframe
fig = px.scatter(DF1, x="population",
                       y="Tipo_Vivienda",
	                   size="population",
                       color="Entidad",
                       hover_name="Entidad",
                       log_x=True,
                       size_max=100)
fig.show()