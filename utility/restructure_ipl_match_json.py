import json
import pprint
import os

path = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\json\\all_match_diff_json"

os.chdir(path)

for file in os.listdir():
    print(file)
    if (file.endswith(".json")):
        JsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\json\\all_match_diff_json\\{0}".format(file)

        with open(JsonFilePath, 'r') as jsonf:
            balls = json.load(jsonf)

        newDict = {}
        match_meta_Data = balls.get("balls")[1]
        # pprint.pprint(match_meta_Data)

        newDict["season"] = match_meta_Data.get("season")
        newDict["match_id"] = match_meta_Data.get("match_id")
        newDict["match_name"] = match_meta_Data.get("match_name")
        newDict["home_team"] = match_meta_Data.get("home_team")
        newDict["away_team"] = match_meta_Data.get("away_team")
        newDict["innings"] = []
        newDict.get("innings").append(dict())
        newDict.get("innings").append(dict())
        newDict.get("innings")[0]["innings_id"] = "1"
        newDict.get("innings")[0]["balls"] = []
        newDict.get("innings")[1]["innings_id"] = "2"
        newDict.get("innings")[1]["balls"] = []

        for ball in balls.get("balls"):
            ballDetails = dict()
            ballDetails["over"] = ball.get("over")
            ballDetails["ball"] = ball.get("ball")
            ballDetails["runs"] = ball.get("runs")
            ballDetails["shortText"] = ball.get("shortText")
            ballDetails["isBoundary"] = ball.get("isBoundary")
            ballDetails["isWide"] = ball.get("isWide")
            ballDetails["isNoball"] = ball.get("isNoball")
            ballDetails["batsman1_id"] = ball.get("batsman1_id")
            ballDetails["batsman1_name"] = ball.get("batsman1_name")
            ballDetails["batsman1_runs"] = ball.get("batsman1_runs")
            ballDetails["batsman1_balls"] = ball.get("batsman1_balls")
            ballDetails["bowler1_id"] = ball.get("bowler1_id")
            ballDetails["bowler1_name"] = ball.get("bowler1_name")
            ballDetails["bowler1_overs"] = ball.get("bowler1_overs")
            ballDetails["bowler1_maidens"] = ball.get("bowler1_maidens")
            ballDetails["bowler1_runs"] = ball.get("bowler1_runs")
            ballDetails["bowler1_wkts"] = ball.get("bowler1_wkts")
            ballDetails["batsman2_id"] = ball.get("batsman2_id")
            ballDetails["batsman2_name"] = ball.get("batsman2_name")
            ballDetails["batsman2_runs"] = ball.get("batsman2_runs")
            ballDetails["batsman2_balls"] = ball.get("batsman2_balls")
            ballDetails["bowler2_id"] = ball.get("bowler2_id")
            ballDetails["bowler2_name"] = ball.get("bowler2_name")
            ballDetails["bowler2_overs"] = ball.get("bowler2_overs")
            ballDetails["bowler2_maidens"] = ball.get("bowler2_maidens")
            ballDetails["bowler2_runs"] = ball.get("bowler2_runs")
            ballDetails["bowler2_wkts"] = ball.get("bowler2_wkts")
            ballDetails["wicket_id"] = ball.get("wicket_id")
            ballDetails["wkt_batsman_name"] = ball.get("wkt_batsman_name")
            ballDetails["wkt_bowler_name"] = ball.get("wkt_bowler_name")
            ballDetails["wkt_batsman_runs"] = ball.get("wkt_batsman_runs")
            ballDetails["wkt_batsman_balls"] = ball.get("wkt_batsman_balls")
            ballDetails["wkt_text"] = ball.get("wkt_text")
            ballDetails["isRetiredHurt"] = ball.get("isRetiredHurt")
            ballDetails["comment_id"] = ball.get("comment_id")
            ballDetails["text"] = ball.get("text")
            ballDetails["preText"] = ball.get("preText")
            ballDetails["postText"] = ball.get("postText")

            if (ball.get("innings_id") == "1"):
                newDict.get("innings")[0]["balls"].append(ballDetails)
                newDict.get("innings")[0]["current_innings"] = ball.get("current_innings")
            if (ball.get("innings_id") == "2"):
                newDict.get("innings")[1]["balls"].append(ballDetails)
                newDict.get("innings")[1]["current_innings"] = ball.get("current_innings")

        writeJsonFilePath = "C:\\Users\\1021053\\Documents\\Spring_Practice\\IPL\\json\\all_match_diff_json\\pretty\\{0}".format(file)
        with open(writeJsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(newDict, indent=4))

