import cricket_utils

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
matchSummary['home_team_playing_11'] = homeTeam_playing11.read().split()
matchSummary['guest_team_playing_11'] = guestTeam_playing11.read().split()

# Finding score of each team
with open("matchDetails.txt", "w") as file:
    matchSummary["innings1_score"] = cricket_utils.ballByBall(matchSummary, 1, file)
    matchSummary["innings2_score"] = cricket_utils.ballByBall(matchSummary, 2, file)

# Deciding the winner of each team
matchSummary["match_winner"] = cricket_utils.winner(matchSummary)
print(matchSummary)
