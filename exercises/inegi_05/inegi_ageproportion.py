import pandas as pd
import matplotlib.pyplot as plt

#Reading dataset csv file
data = pd.read_csv("/home/luis/proyectos/python/python_exercises/resources/inegi2010/conjunto_de_datos/iter_00_cpv2010.csv", sep=",", encoding="utf-8")

# Select columns to use
data = data.filter(["entidad","mun","loc","p_3a5","p_6a11","p_8a14","p_12a14","p_15a17","p_18a24","p_60ymas"])
data['entidad'] = pd.to_numeric(data['entidad'], errors='coerce')
data['mun'] = pd.to_numeric(data['mun'], errors='coerce')
data['loc'] = pd.to_numeric(data['loc'], errors='coerce')
data['p_3a5'] = pd.to_numeric(data['p_3a5'], errors='coerce')
data['p_6a11'] = pd.to_numeric(data['p_6a11'], errors='coerce')
data['p_8a14'] = pd.to_numeric(data['p_8a14'], errors='coerce')
data['p_12a14'] = pd.to_numeric(data['p_12a14'], errors='coerce')
data['p_15a17'] = pd.to_numeric(data['p_15a17'], errors='coerce')
data['p_18a24'] = pd.to_numeric(data['p_18a24'], errors='coerce')
data['p_60ymas'] = pd.to_numeric(data['p_60ymas'], errors='coerce')
data.fillna(0, inplace=True)

# Valid states of Mexico, we remove id 0 because this one belongs to the total of the column
data = data.loc[(data['entidad'] == 0) & (data['mun'] == 0) & (data['loc'] == 0)]

total = data['p_3a5'] + data['p_6a11'] + data['p_8a14'] + data['p_12a14'] + data['p_15a17'] + data['p_18a24'] + data['p_60ymas']


#print(data)
print(total)
print((data['p_3a5'] * 100)/total)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '3 a 5 años', '6 a 11 años', '8 a 14 años', '12 a 14 años', '15 a 17 años', '18 a 24 años', '60 años y más'
sizes = [(data['p_3a5'] * 100)/total,
         (data['p_6a11'] * 100)/total,
         (data['p_8a14'] * 100)/total,
         (data['p_12a14'] * 100)/total,
         (data['p_15a17'] * 100)/total,
         (data['p_18a24'] * 100)/total,
         (data['p_60ymas'] * 100)/total]
explode = (0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Distribución de población por edad", bbox={'facecolor':'0.8', 'pad':1})
plt.show()