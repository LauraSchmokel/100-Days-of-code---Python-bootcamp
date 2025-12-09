import art
import os

print(art.art)

players = {}

answer = True
while answer != False:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    players[name] = bid

    other_players= ""
    while other_players != "yes" and other_players != "no":
        other_players = input("Are ther any other bidders? Type 'yes' or 'no': ")   

    if other_players == "no":
        answer = False
        bids = players.values()
        names = players.keys()
        highest_bid = list(bids).index(max(bids))
        print(f"The winner is {list(names)[highest_bid]} with a bid of ${list(bids)[highest_bid]}!")

    elif other_players == "yes":
        os.system("cls")
