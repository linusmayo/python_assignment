import json
import csv

# JSON and CSV Reading
stations_csv = csv.DictReader(open("stations.csv"))

# Creates a list of station codes
stations = []
for city in stations_csv:
    stations.append(city["Station"]) 

file = open("precipitation.json")
precipitation = json.load(file)
#----------------------------------------------------
output = {}

# Loops through the 4 city codes in the stations list created above
for code in stations:
    city = {}
    seattle_precipitation = []

    total_yearly_precipitation = 0
    # Loops through all the dictionaries in precipitation
    for event in precipitation:
        if event["station"] == code: # Verifies the station code of each city
            event["date"] = event["date"].split("-")

            # Appends a list in which each event of Seattle is contained
            seattle_precipitation.append(event)
            
            # Adds the value for each event to the running total
            total_yearly_precipitation += event["value"]

    # Loops through all the events in Seattle, adds the value to the corresponding month
    total_monthly_precipitation = [0]*12
    for event in seattle_precipitation:
        total_monthly_precipitation[int(event['date'][1]) - 1] += event['value']

    # Calculates monthly relative precipitation
    monthly_relative_precipitation = []
    for month in total_monthly_precipitation:
        month_relative = month / total_yearly_precipitation
        monthly_relative_precipitation.append(month_relative)

    # Creates an entry in the output dictionary for the city
    output["Location"] = city

    # Plugs the data for the city underneath its final output key
    city["Monthly Precipitation"] = total_monthly_precipitation
    city["Yearly Precipitation"] = total_yearly_precipitation
    city["Relative Monthly Precipitation"] = monthly_relative_precipitation
    

#Creates results.json file to hold the output data
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, indent = 4)
        

# I was not finished with this code, but was planning on finishing it so that the output was correctly displayed for all four
# cities in the results.json output. It is correctly displayed with a print() command, however. 
