import json
import os
import pprint
import  math

total = 0
boundaries = 0
deliveriesPercentageBoundaries = {}

path_to_json = "C:\\cricket_data\\t20s_json"

print(len(os.listdir(path_to_json)))

for json_file in os.listdir((path_to_json)):
    jsonFilePath = "C:\\cricket_data\\t20s_json\\{fileName}".format(fileName=json_file)
    with open(jsonFilePath, 'r') as f:
        fileData = json.load(f)

    # Going through each innings
    for inning in fileData.get("innings"):
        for over in inning.get("overs"):
            for deliveryNumber in range(len(over.get("deliveries"))):
                if (deliveryNumber <= 5):
                    if (deliveriesPercentageBoundaries.get(
                            str(over.get("over")) + "." + str(deliveryNumber)) is None):
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)] = [0, 0, 0,
                                                                                                             dict()]
                    if (over.get("deliveries")[deliveryNumber].get("runs").get("total") >= 4):

                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0] += 1;
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] += 1;
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][2] = \
                            (deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] /
                             deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0]) * 100
                        if deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][3].get(
                                (over.get("deliveries")[deliveryNumber].get("batter"))) is not None:
                            deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][3][
                                (over.get("deliveries")[deliveryNumber].get("batter"))] += 1
                        else:
                            deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][3][
                                (over.get("deliveries")[deliveryNumber].get("batter"))] = 1


                    else:
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0] += 1;
                        deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][2] = \
                            (deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][1] /
                             deliveriesPercentageBoundaries[str(over.get("over")) + "." + str(deliveryNumber)][0]) * 100

resultDict = {}
for deliveryData in deliveriesPercentageBoundaries.items():
    resultDict[deliveryData[0]] = deliveryData[1][2]

new_file = open("t20s_analysis.txt", mode="w", encoding="utf-8")
for deliveryData in sorted(resultDict.items(), key=lambda  item:item[1]):
# for deliveryData in resultDict.items():
    players = deliveriesPercentageBoundaries.get(deliveryData[0])[3]

    deliveryString = "\n" + "Ball: " +  str(deliveryData[0]) + " Chances: " + str(round(deliveryData[1], 2)) + " Total : " + str(
        deliveriesPercentageBoundaries.get(deliveryData[0])[0]) + " Boundaries: " + str(
        deliveriesPercentageBoundaries.get(deliveryData[0])[1]) + "\n"
    new_file.write(deliveryString)
    new_file.write(str(sorted(players.items(), key=lambda item: item[1], reverse=True)))
new_file.close()
