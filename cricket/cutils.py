
import random

def toss(home, away):
    selected_coin_side = input("Away team please select head/tails 0/1")
    des = random.randint(0, 1)
    print("Toss result is Head" if des == 0 else "Toss result is Tails")
    if int(selected_coin_side) == des:
        print(away, " team won the toss.")
        return away
    else:
        print(away, " team won the toss.")
        return home