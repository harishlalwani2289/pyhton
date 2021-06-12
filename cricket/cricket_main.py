import random
import cutils

matchSummary = {}

homeTeam = input("Enter home team name:-")
matchSummary["homeTeam"] = homeTeam

awayTeam = input("Enter away team name:-")
matchSummary["awayTeam"] = awayTeam

matchSummary["tossWinner"] = cutils.toss(homeTeam, awayTeam)
print(matchSummary)

#Now we want the toss winning team to make a choice to bat or ball
matchSummary["tossDecision"] = cutils.tossDecision()

# homeTeamPlayer = {}
# n = int(input("number of player for home team:-"))
# for a in range(n):
#     no = int(input("Enter serial no:-"))
#     plyar = input(("Enter home team Player name:-"))
#     homeTeamPlayer.update({no: plyar})
# # print(homeTeamPlayer)
#
# awayTeamPlayer = {}
# print("")
# n = int(input("number of player for away team:-"))
# for a in range(n):
#     no = int(input("Enter serial no:-"))
#     plyar = input(("Enter away team Player name:-"))
#     awayTeamPlayer.update({no: plyar})
#
# print("Home team player list")
# print(homeTeamPlayer)
#
# print("")
#
# print("Away team player list")
# print(awayTeamPlayer)
