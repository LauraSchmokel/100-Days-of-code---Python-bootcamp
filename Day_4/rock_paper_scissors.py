import random
# import my_module

# random_int = random.randint(1, 10)

# print(random_int)
# print(my_module.my_favorite_number)

# print(random.uniform(1, 10))

# rand_num = random.randint(0,1)

# if rand_num == 1:
#     print("Heads")

# else:
#     print("Tails")

# --------------

# states_us = ["Delaware", "Pennsylvania", "New Jersey"]

# # print(states_us[0])

# states_us[1] = "Pencilvania"

# states_us.append("Laura")
# states_us.extend(["example1", "example2"])

# print(states_us)



# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# person = random.randint(0, len(friends))

# print(f"{friends[person]} will pay the bill!")

# --------------

# fruits = ["Apples", "Grapes", "Peaches"]
# vegetables = ["Spinach", "Tomatoes", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen)

# ROCK PAPER SCISSORS

player = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors "))
choices = ["Rock", "Paper", "Scissors"]

computer = random.randint(0, 2)

if player >2 or player <0:
    print("You typed an invalid number! You lose!")

elif player == computer:
    print(f"Computer chose: {choices[computer]}")
    print("Draw!")

elif player == 0 and computer == 2:
    print(f"Computer chose: {choices[computer]}")
    print("You win")

elif player == 2 and computer == 0:
    print(f"Computer chose: {choices[computer]}")
    print("You lose")

elif computer > player:
    print(f"Computer chose: {choices[computer]}")
    print("You lose")

elif player > computer:
    print(f"Computer chose: {choices[computer]}")
    print("You win")

