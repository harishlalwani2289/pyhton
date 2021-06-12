import csv
import json
import os

path = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\2021\\2021"

os.chdir(path)

data = {}

for file in os.listdir():
    print(file)
    if (file.endswith(".csv")):
        csvFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\2021\\2021\\{0}".format(file)
        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            ballsList = []
            data["balls"] = ballsList
            for rows in csvReader:
                data["balls"].append(rows)
        jsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\2021\\2021\\json\\{0}.json".format(file[0:file.index(".")])
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))