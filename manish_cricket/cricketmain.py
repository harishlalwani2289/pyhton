import cricket_utils

# Creating match summary dictionary
matchSummary = {}

# Taking team name input from user
cricket_utils.inputTeamNames(matchSummary)

# Toss Process
matchSummary["tossWinner"] = cricket_utils.toss(matchSummary.get("hometeam"), matchSummary.get("guestteam"))
cricket_utils.tossDecisionProcess(matchSummary)

# Read team list from file
homeTeam_playing11 = open('hometeam.txt')
guestTeam_playing11 = open('guestteam.txt')
matchSummary['home_team_playing_11'] = homeTeam_playing11.read().split()
matchSummary['guest_team_playing_11'] = guestTeam_playing11.read().split()

# Finding score of each team
matchSummary["innings1_score"] = cricket_utils.ballByBall(matchSummary, 1)
matchSummary["innings2_score"] = cricket_utils.ballByBall(matchSummary, 2)

# Deciding the winner of each team
matchSummary["match_winner"] = cricket_utils.winner(matchSummary)
print(matchSummary)
