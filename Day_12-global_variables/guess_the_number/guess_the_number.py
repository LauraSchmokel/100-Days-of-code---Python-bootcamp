import art
import random

RANDOM_NUMBER = random.randint(0, 100)
DIFFICULTY = ['easy', 'hard']

def check_number (guess, attempts):
    if guess == RANDOM_NUMBER:
        print("\nYou won!")
        return True, attempts

    attempts -= 1

    if attempts == 0:
        print(f"\nYou have {attempts} attempts.\n\nYou lose :(")
        return False, attempts

    elif guess > RANDOM_NUMBER:
        print("\nToo high!")
        
        print(f"You have {attempts} attempts to guess the number!\n")
        return False, attempts
    
    elif guess < RANDOM_NUMBER:
        print("\nToo low!")
        print(f"You have {attempts} attempts to guess the number!\n")
        return False, attempts
    
print(art.logo)

difficulty = input("Choose the difficulty:\n\nType 'easy' or 'hard': ")

while difficulty not in DIFFICULTY:
    difficulty = input("\nChoose one of the following difficulty:\n\nType 'easy' or 'hard': ")
    
attempts = 10 if difficulty == 'easy' else 5

print(f"\nYou have {attempts} attempts to guess the number!")

is_number_correct = False

while not is_number_correct:

    try:
        players_number = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        players_number = int(input("Type a number between 1 and 100! "))

    is_number_correct, attempts = check_number(players_number, attempts)

