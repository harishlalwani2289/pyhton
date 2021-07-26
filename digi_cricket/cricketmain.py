import cricket_utils
import pprint

# Creating match summary dictionary
matchSummary = {}

# Taking team name input from user
cricket_utils.inputTeamNames(matchSummary)

# Toss Process
matchSummary["tossWinner"] = cricket_utils.toss(matchSummary.get("hometeam"), matchSummary.get("guestteam"))
cricket_utils.toss_decision_process(matchSummary)

# Read team list from file
homeTeam_playing11 = open('hometeam.txt')
guestTeam_playing11 = open('guestteam.txt')
matchSummary[matchSummary.get("hometeam") + '_playing_11'] = homeTeam_playing11.read().split("\n")
matchSummary[matchSummary.get("guestteam") + '_playing_11'] = guestTeam_playing11.read().split("\n")

# Finding score of each team
with open("matchDetails.txt", "w") as file:
    with open("ballDetails.csv", 'w', newline='') as ballDetailsFile:
        matchSummary["innings1_score"] = cricket_utils.ballByBall(matchSummary, 1, file)
        matchSummary["innings2_score"] = cricket_utils.ballByBall(matchSummary, 2, file)

# Deciding the winner of each team
matchSummary["match_winner"] = cricket_utils.winner(matchSummary)
pprint.pprint(matchSummary)
