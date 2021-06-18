import random


def ballByBall(matchSummary, inningsNumber):
    balldata = [0, 1, 2, 3, 4, 5, 6, "wd", "nb", "w"]
    w = 0
    totalruns = 0
    balls = 0
    while balls < 60 and w < 10:
        balls = balls + 1
        cb = random.choices(balldata, weights=[10, 12, 8, 4, 5, 4, 3, 1, 1, 4], k=1)
        print("InningsNumber{2}, Ball Number {0}, Result : {1}".format(balls, cb, inningsNumber))

        if cb[0] == "wd" or cb[0] == "nb":

            totalruns = totalruns + 1
            balls = balls - 1
        elif cb[0] == 0:
            totalruns = totalruns + 0


        elif cb[0] == 1:
            totalruns = totalruns + 1

        elif cb[0] == 2:
            totalruns = totalruns + 2

        elif cb[0] == 3:

            totalruns = totalruns + 3
        elif cb[0] == 4:

            totalruns = totalruns + 4
        elif cb[0] == 5:

            totalruns = totalruns + 5
            balls = balls - 1
        elif cb[0] == 6:

            totalruns = totalruns + 6
        else:
            w = w + 1

    return totalruns
