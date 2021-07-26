import random
import cutils
import time

matchSummary = {}

homeTeam = input("Enter home team name:-")
matchSummary["homeTeam"] = homeTeam
time.sleep(4)


awayTeam = input("Enter away team name:-")
matchSummary["awayTeam"] = awayTeam

matchSummary["tossWinner"] = cutils.toss(homeTeam, awayTeam)

#Now we want the toss winning team to make a choice to bat or ball
matchSummary["tossDecision"] = cutils.toss_Decision()

file_home_playing_eleven = open("home_eleven.txt")
matchSummary["home_playing_eleven"] = file_home_playing_eleven.read().split()
print(matchSummary)

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
