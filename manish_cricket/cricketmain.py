import random
import ck


def toss(hometeam, guestteam):
    guestteam_choose = int(input("please choose 1 for head and 0 for tails"))
    coin_face = random.randint(0, 1)
    print(coin_face)
    if coin_face == guestteam_choose:
        print("guest team choose", guestteam_choose, "and won the toss ")
        return guestteam
    else:
        print("guest team chose", guestteam_choose, "loss but home team won the toss")
        return hometeam


def selection():
    selected = input("Batfirst or Ball First")
    return selected


def winner():
    winner = ""
    if matchsum["hometeam_score"] > matchsum["guestteam_score"]:

        winner = matchsum["hometeam"]
    elif matchsum["hometeam_score"] < matchsum["guestteam_score"]:
        winner = matchsum["guestteam"]
    else:
        winner = "both team score is same so the match is draw"

    return winner


matchsum = {}
hometeam = input("please enter home team name")
guestteam = input("please enter guest team name")
matchsum["hometeam"] = hometeam
matchsum["guestteam"] = guestteam
matchsum["toss winner"] = toss(hometeam, guestteam)
# print("comentery",matchsum)
matchsum["selected to"] = selection()
hometeam_playingxi = open('hometeam.txt')
guestteam_playingxi = open('guestteam.txt')
matchsum['hometeamplayingxi'] = hometeam_playingxi.read().split()
matchsum['guestteamplayingxi'] = guestteam_playingxi.read().split()
matchsum["hometeam_score"] = ck.ballByBall(matchsum, 1)
matchsum["guestteam_score"] = ck.ballByBall(matchsum, 2)
matchsum["match_winner"] = winner()
print(matchsum)
