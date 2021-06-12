import json
import pprint

jsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\2021\\2021\\json\\season_details.json"

with open(jsonFilePath, 'r') as f:
    fileData = json.load(f)

print(type(fileData))
match_id_set = set()
for ball in fileData.get("balls"):
    match_id_set.add(ball.get("match_id"))


for match_id in match_id_set:
    currentMatch = {"balls" : []}
    for ball in fileData.get("balls"):
        if (ball.get("match_id") == match_id):
            currentMatch.get("balls").append(ball)
    writeJsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\json\\all_match_diff_json\\{0}".format(match_id + ".json")
    with open(writeJsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(currentMatch, indent=4))