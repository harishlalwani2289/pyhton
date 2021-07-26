import random
import csv


def ballByBall(matchSummary, inningsNumber, file):
    ball_results = [0, 1, 2, 3, 4, 5, 6, "wd", "nb", "w"]
    w = 0
    total_runs = 0
    balls = 0

    if inningsNumber == 1:
        file.write("{0} Batting\n".format(matchSummary.get("innings1")))
        player_to_bat = list(matchSummary.get(matchSummary.get("innings1") + '_playing_11')).copy()
        print("Player to Bat :", player_to_bat)
        wickets = []
        striker = player_to_bat.pop(0)  # First player in list
        non_striker = player_to_bat.pop(0)  # First player in list, which is actually 2nd player to bat
        file_mode = 'w'
    else:
        file.write("{0} Batting\n".format(matchSummary.get("innings2")))
        player_to_bat = list(matchSummary.get(matchSummary.get("innings2") + '_playing_11')).copy()
        print("Player to Bat :", player_to_bat)
        wickets = []
        striker = player_to_bat.pop(0)
        non_striker = player_to_bat.pop(0)
        file_mode = 'a'

    with open("ballDetails.csv", file_mode, newline='') as ballDetailsFile:
        writer = csv.writer(ballDetailsFile)
        if (file_mode == 'w'): writer.writerow(["InningsNumber", "Ball Number", "Ball Result", "Batsman"])
        # Running balls one by one
        while balls < 60 and w < 10:

            # Incrementing the ball
            balls = balls + 1

            # Getting current ball result
            current_ball_result = random.choices(ball_results, weights=[10, 12, 8, 4, 5, 4, 3, 1, 1, 4], k=1)

            # Storing the ball details
            writer.writerow([inningsNumber, balls, current_ball_result[0], striker])

            # Commentary printing
            file.write(
                "Innings Number {2},Batsman {3} Ball Number {0}, Result : {1}\n".format(balls, current_ball_result[0],
                                                                                        inningsNumber, striker))

            # Updating total runs and wickets as required
            if current_ball_result[0] == "wd" or current_ball_result[0] == "nb":
                total_runs = total_runs + 1
                balls = balls - 1
            elif current_ball_result[0] == "w":
                w = w + 1
                wickets.append(striker)
                striker = player_to_bat.pop(0)
            else:
                total_runs = total_runs + current_ball_result[0]
                if (current_ball_result[0] % 2 == 0 and balls % 6 == 0) or (current_ball_result[0] % 2 != 0 and balls % 6 != 0):
                    striker, non_striker = non_striker, striker

            # Checking if second batting team has won the match
            if inningsNumber == 2 and total_runs > \
                    int(matchSummary.get("innings1_score")[0:matchSummary.get("innings1_score").index("-")]):
                print("Innings 2 wickets : {0}".format(wickets))
                return str(total_runs) + "-" + str(w)
    print("Innings " + str(inningsNumber) + " wickets : {0}".format(wickets))
    return str(total_runs) + "-" + str(w)


def toss(homeTeam, guestTeam):
    guestTeam_choose = int(input("please choose 1 for head and 0 for tails"))
    coin_face = random.randint(0, 1)
    print(coin_face)
    if coin_face == guestTeam_choose:
        print(guestTeam, "chose", "Head" if guestTeam_choose == 1 else "Tails", "and won the toss ")
        return guestTeam
    else:
        print(guestTeam, "chose", "Head" if guestTeam_choose == 1 else "Tails", "and lost the toss ")
        print(homeTeam, "won the toss")
        return homeTeam


def toss_decision_process(matchSummary):
    selected = input("Bat first or Ball First")
    matchSummary["tossDecision"] = selected
    if matchSummary.get("tossWinner") == matchSummary.get("guestteam") and selected == "Bat":
        matchSummary["innings1"] = matchSummary.get("guestteam")
        matchSummary["innings2"] = matchSummary.get("hometeam")
    elif matchSummary.get("tossWinner") == matchSummary.get("guestteam") and selected == "Ball":
        matchSummary["innings1"] = matchSummary.get("hometeam")
        matchSummary["innings2"] = matchSummary.get("guestteam")
    elif matchSummary.get("tossWinner") == matchSummary.get("hometeam") and selected == "Bat":
        matchSummary["innings1"] = matchSummary.get("hometeam")
        matchSummary["innings2"] = matchSummary.get("guestteam")
    elif matchSummary.get("tossWinner") == matchSummary.get("hometeam") and selected == "Ball":
        matchSummary["innings1"] = matchSummary.get("guestteam")
        matchSummary["innings2"] = matchSummary.get("hometeam")

    print("{0} will Bat First,{1} will ball first".format(matchSummary.get("innings1"), matchSummary.get("innings2")))


def winner(matchSummary):
    """
    Takes the match Summary as input and return the wining team based on
    score of each teams.
    :param matchSummary: Containing the information about match with individual team scores
    :return: winner of the Match
    """
    if matchSummary["innings1_score"] > matchSummary["innings2_score"]:
        match_winner = matchSummary["innings1"]
    elif matchSummary["innings1_score"] < matchSummary["innings2_score"]:
        match_winner = matchSummary["innings2"]
    else:
        match_winner = "both team score is same so the match is tie"

    return match_winner


def inputTeamNames(matchSummary):
    hometeam = input("please enter home team name")
    guestteam = input("please enter guest team name")
    matchSummary["hometeam"] = hometeam
    matchSummary["guestteam"] = guestteam
