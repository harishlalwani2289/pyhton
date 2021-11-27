import json
import os
import pprint

total = 0
boundaries = 0
deliveriesPercentageBoundaries = {}

path_to_json = "C:\\cricket_data\\ipl_json"

print(len(os.listdir(path_to_json)))

for json_file in os.listdir((path_to_json)):
    jsonFilePath = "C:\\cricket_data\\ipl_json\\{fileName}".format(fileName=json_file)
    with open(jsonFilePath, 'r') as f:
        fileData = json.load(f)

    # Going through each innings
    for inning in fileData.get("innings"):
        for over in inning.get("overs"):
            for deliveryNumber in range(len(over.get("deliveries"))):
                if(deliveryNumber <= 5):
                    if (deliveriesPercentageBoundaries.get(
                            str(over.get("over")) + "." + str(deliveryNumber)) is None):
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)] = [0, 0, 0]
                    if (over.get("deliveries")[deliveryNumber].get("runs").get("total") >= 4):

                            deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0] += 1;
                            deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] += 1;
                            deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][2] = \
                                (deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] /
                                 deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0]) * 100
                    else:
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0] += 1;
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][2] = \
                            (deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] /
                             deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0]) * 100

resultDict ={}
for deliveryData in deliveriesPercentageBoundaries.items():
    resultDict[deliveryData[0]] = deliveryData[1][2]

for deliveryData in sorted(resultDict.items(), key=lambda item: item[1]):
    print(deliveryData)