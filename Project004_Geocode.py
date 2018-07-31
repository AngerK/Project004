#! python3
# Project004_Geocode.py

"""
This script obtains geocoding data from an address batch file.
https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.pdf
"""

import requests, pandas as pd, io, sqlite3

url = 'https://geocoding.geo.census.gov/geocoder/locations/addressbatch'
payload = {'benchmark':'Public_AR_Current','vintage':'ACS2013_Current'}
files = {'addressFile': ('Project004_Geocode_Batch_NYSports.txt', open('Project004_Geocode_Batch_NYSports.txt', 'rb'), 'text/csv')}
r = requests.post(url, files=files, data=payload)

df = pd.read_csv(io.StringIO(r.text), names=['ID',
                                             'Input_Address',
                                             'Match?',
                                             'Match_Type',
                                             'Match_Address',
                                             'Longitude_Latitude',
                                             'tigerLine_ID',
                                             'Side_of_Street'])

conn = sqlite3.connect('Project004.db')

df.to_sql("Responses", conn, if_exists="append")
