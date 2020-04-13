import pandas as pd
import csv
import numpy as np
import folium
from folium import *
import plotly.express as px
from ipywidgets import interact


# loading data from the source:
deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
country = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv')

# renaming the df column names to lowercase
country.columns = map(str.lower, country.columns)
confirmed.columns = map(str.lower, confirmed.columns)
deaths.columns = map(str.lower, deaths.columns)
recovered.columns = map(str.lower, recovered.columns)

# changing province/state to state and country/region to country
confirmed = confirmed.rename(columns={'province/state': 'state', 'country/region': 'country'})
recovered = recovered.rename(columns={'province/state': 'state', 'country/region': 'country'})
death = deaths.rename(columns={'province/state': 'state', 'country/region': 'country'})
country = country.rename(columns={'country_region': 'country'})
country = country.drop([60, 109], axis=0)

#total number of confirmed cases, deaths, recovered and active
confirmed_total = int(country['confirmed'].sum())
deaths_total = int(country['deaths'].sum())
recovered_total = int(country['recovered'].sum())
active_total = int(country['active'].sum())

# creating world map using Map class
corona_map = folium.Map(location=[11,0], tiles="openstreetmap", zoom_start=2, max_zoom = 7, min_zoom = 2)
# iterate over all the rows of confirmed_df to get the lat/long
for i in range(0,len(country)):
    folium.Circle(
        location=[country.iloc[i]['lat'], country.iloc[i]['long_']],
        fill=True,
        radius=(int((np.log(country.iloc[i,4]+1.00001)))+0.2)*10000,
        color='red',
        fill_color='indigo',
        tooltip="{0} , {1}".format(country.iloc[i][0], country.iloc[i][4])
    ).add_to(corona_map)
    
corona_map.save('./corona_map.html')