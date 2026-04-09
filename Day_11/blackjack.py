import art
import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

players_cards = []
dealers_cards = []

def options():
    print("""
1. Start Game
2. Finish Game
""")
    option = int(input("Choose an option: "))

    return option

def pontuation(dealers_cards, dealers_sum, players_sum):
    print(f"\nDealer's cards: {dealers_cards}")
    print(f"Dealer's total: {dealers_sum}")
    print(f"\nYour total: {players_sum}")


print(art.logo)

option = options()

while option == 1:
    for i in range (0, 3):
        if i == 2:
            dealers_cards.append(cards[random.randint(0, len(cards)-1)])
            dealers_cards.append("?")

        else: 
            players_cards.append(cards[random.randint(0, len(cards)-1)])
            

    print(f"\nYour cards: {players_cards}")
    print(f"\nDealer's cards: {dealers_cards}")


    
    print("""
    1. Hit
    2. Stand
    """)

    choice = input("choose an option: ")

    if choice == 1:
        pass

    else:
        dealers_cards[dealers_cards.index('?')] = cards[random.randint(0, len(cards)-1)]

        players_sum = sum(players_cards)
        dealers_sum = sum(dealers_cards)

        if players_sum > 21 and 11 in players_cards:
                players_cards[players_cards.index(11)] = 1

        elif dealers_sum > 21 and 11 in dealers_cards:
                dealers_cards[dealers_cards.index(11)] = 1

        else:
            if dealers_sum > 21 or (players_sum > dealers_sum and players_sum <=21):
                pontuation(dealers_cards=dealers_cards, dealers_sum = dealers_sum, players_sum = players_sum)
                print(f"\n {art.win}")


            elif players_sum > 21 or (dealers_sum > players_sum and dealers_sum <=21):
                pontuation(dealers_cards=dealers_cards, dealers_sum = dealers_sum, players_sum = players_sum)

                print(f"\n {art.lose}")


            elif players_sum == dealers_sum or (dealers_sum > 21 and players_sum > 21):
                pontuation(dealers_cards=dealers_cards, dealers_sum = dealers_sum, players_sum = players_sum)

                print(f"\n {art.draw}")

    option = options()

print("\nEnding game...")