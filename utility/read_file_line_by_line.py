
import pprint
with open("demofile3.txt", mode="r", encoding="utf-16") as f:
        pprint.pprint([line.strip() for line in f])