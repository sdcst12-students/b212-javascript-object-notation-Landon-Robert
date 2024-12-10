import requests
import json

req = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m')
data = req.text
importedData = json.loads(data)
print(importedData)

for i in importedData:
    if importedData[i].index() < 6:
        print(importedData.capitalize(i))