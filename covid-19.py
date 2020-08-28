import pandas as pd
import numpy as np
import folium
from folium import *

# loading data from the source:
country = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

# renaming the df column names to lowercase
country.columns = map(str.lower, country.columns)
#print(country.to_string())
# changing column name from country/region to country
country = country.rename(columns={'country_region': 'country'})

country = country.drop([48, 104], axis=0)
print(country.to_string())
# creating world map using Map class
corona_map = folium.Map(location=[11,0], tiles="openstreetmap", zoom_start=2, max_zoom = 7, min_zoom = 2)
# iterate over all the rows of confirmed_df to get the lat/long
for i in range(0,len(country)):
    folium.Circle(
        location=[country.iloc[i]['lat'], country.iloc[i]['long_']],
        fill=True,
        radius=(int((np.log(country.iloc[i,4]+1.00001)))+0.2)*13000,
        color='red',
        fill_color='indigo',
        tooltip="{0} , {1} confirmed cases".format(country.iloc[i][0], int(country.iloc[i][4]))
    ).add_to(corona_map)
    folium.Circle(
        location=[country.iloc[i]['lat'], country.iloc[i]['long_']],
        fill=True,
        radius=(int((np.log(country.iloc[i,5]+1.00001)))+0.2)*6000,
        color='blue',
        fill_color='blue',
        tooltip="{0} , {1} deaths".format(country.iloc[i][0], int(country.iloc[i][5]))
    ).add_to(corona_map)
   
    
corona_map.save('./corona_map.html')