#! python3
# Project004_Geocode_ReadSQL.py

"""
This script runs a SQL query.
"""

import sqlite3, pandas as pd

conn = sqlite3.connect('Project004.db')

results = pd.read_sql_query("select * from Responses;", conn)

print(results)
