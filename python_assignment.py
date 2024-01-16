import json
import csv

# JSON and CSV Reading
stations_csv = csv.DictReader(open("stations.csv"))
stations = []
for city in stations:
    stations.append("Station")

seattle = open("precipitation.json")
precipitation = json.load(seattle)
#----------------------------------------------------
output = {}
seattle = {}
output["Seattle"] = seattle
seattle_precipitation = []
total_yearly_precipitation = 0

# Loops through all the dictionaries in precipitation
for event in precipitation:
    if event["station"] == "GHCND:US1WAKG0038": # Ensures that 
        event["date"] = event["date"].split("-")

        # Appends a list in which each event of Seattle is contained
        seattle_precipitation.append(event)
        
        total_yearly_precipitation += event["value"]

# Loops through all the events in Seattle, adds the value to the corresponding month
month_total = [0]*12
seattle["Monthly Precipitation"] = month_total
for event in seattle_precipitation:
    month_total[int(event['date'][1]) - 1] += event['value']

monthly_relative_precipitation = []
for month in month_total:
    month_relative = month / total_yearly_precipitation
    monthly_relative_precipitation.append(month_relative)

seattle["Yearly Precipitation"] = total_yearly_precipitation
seattle["Relative Monthly Precipitation"] = monthly_relative_precipitation

# Creates results.json file to hold the month_total data

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, indent = 4)
        


