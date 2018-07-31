#! python3
# Project004_Geocode_gmaps_Locations.py

"""
This script runs a SQL query.
"""

import gmaps
import gmaps.datasets
import sqlite3, pandas as pd

with open(r'Project004_API_Key.txt') as raw_file:
    apikey = raw_file.read()

gmaps.configure(api_key=apikey)

conn = sqlite3.connect('Project004.db')

results = pd.read_sql_query("select * from Responses;", conn)
latlong = results['Longitude_Latitude'].str.split(',', expand=True)
latlong.columns = ['Long','Lat']
columntitles=['Lat','Long']
latlong = latlong.reindex(columns=columntitles)
latlong = latlong.dropna()
latlong["Lat"] = latlong["Lat"].astype(float)
latlong["Long"] = latlong["Long"].astype(float)

locations = latlong
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations))
fig