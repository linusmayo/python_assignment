import json

seattle = open("precipitation.json")
precipitation = json.load(seattle)

seattle_precipitation = []
month_total = [0,0,0,0,0,0,0,0,0,0,0,0]

for event in precipitation:
    if event["station"] == "GHCND:US1WAKG0038":
        event["date"] = event["date"].split("-")
        seattle_precipitation.append(event)
        for event in seattle_precipitation:
            month_total[int(event['date'][1]) - 1] += event['value']

print(seattle_precipitation)

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(month_total, file, indent = 4)
        


