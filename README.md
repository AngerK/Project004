# Project004
### Heatmaps

The goal is to make heatmaps given a file of addresses.

Put these four files in your current working directory:

Project004_Geocode_v1.py  
Project004_Geocode_v1-1_ReadSQL.py  
Project004_Geocode_v1-2_Jupyter_gmaps.py  
Project004_Geocode_Batch_NYSports.txt

Typing `python Project004_Geocode_v1.py` from the command line will use the addresses in `Project004_Geocode_Batch_NYSports.txt` to obtain Latitude & Longitude from census.gov and store in a sqlite3 database  
Typing `python Project004_Geocode_v1-1_ReadSQL.py` from the command line will read from the sqlite3 database  
The logic from `Project004_Geocode_v1-2_Jupyter_gmaps.py` needs to be in a Jupyter Notebook.  You will need to ensure your notebook is in the proper working directory

When running in Jupyter Notebook you should see something like:


Tested with:  
python 3.6.4  
pandas 0.22.0  
