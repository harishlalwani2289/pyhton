import csv
import json

data = {}

csvFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\points_table.csv"
with open(csvFilePath, encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    ballsList = []
    data["balls"] = ballsList
    for rows in csvReader:
        data["balls"].append(rows)
jsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\points_table.json"
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=4))
