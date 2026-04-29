# Day 14 - Project: Higher or Lower
# Topics: importing modules, random selection, game loops, score tracking
# What I learned: how to structure a game with a continuous loop and track the player's score

import art
import game_data
import random
import subprocess

has_lost = False
score = 0
idx_a = 0
idx_b = 0


def advance_game(idx_a, idx_b):
    idx_a = idx_b
    while idx_a == idx_b:
        idx_b = random.randint(0, len(game_data.data) - 1)

    return idx_a, idx_b

def finish_game(score):
    print(f"You lost!\n\nScore: {score}")
    return True

while idx_a == idx_b:
    idx_a = random.randint(0, len(game_data.data) - 1)
    idx_b = random.randint(0, len(game_data.data) - 1)

while not has_lost:
    answer = ""
    subprocess.run("cls", shell=True) 

    print(art.title_logo)

    print(f"Your score is: {score}")
    print(f"Compare A: {game_data.data[idx_a]['name']}, a {game_data.data[idx_a]['description']}, from {game_data.data[idx_a]['country']}")
    print(art.versus_logo)
    print(f"Compare B: {game_data.data[idx_b]['name']}, a {game_data.data[idx_b]['description']}, from {game_data.data[idx_b]['country']}")

    while answer.upper() not in ('A', 'B'):
         answer = input("Who has more followers? Type 'A' or 'B': ")

    if answer.upper() == 'A':
        if game_data.data[idx_a]['follower_count'] >= game_data.data[idx_b]['follower_count']:
            score += 1
            
            idx_a, idx_b = advance_game(idx_a, idx_b)

        else:
            has_lost = finish_game(score)

    else:
        if game_data.data[idx_b]['follower_count'] >= game_data.data[idx_a]['follower_count']:
            score += 1
            
            idx_a, idx_b = advance_game(idx_a, idx_b)

        else:
            has_lost = finish_game(score)
