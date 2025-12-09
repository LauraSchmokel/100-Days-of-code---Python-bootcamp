import random

# fruits = ["Apple", "Pear", "Orange"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit, "pie")

# print(fruits)

# ---------------------

# student_scores = [5, 8, 4, 10, 9]

# total_exam_score = sum(student_scores)

# sum = 0

# for score in student_scores:
#     sum += score

# print("without for", total_exam_score)
# print("for:", sum)

# ---------------------

# student_scores = [5, 8, 4, 10, 9]

# max_score = max(student_scores)

# max = 0

# for score in student_scores:
#     if score > max:
#         max = score

# print("Without for:", max_score)
# print("for:", max)

# ---------------------
# total = 0

# for number in range(1, 101):
#     total += number

# print(total)
# ---------------------

# SEM UTILIZAR MÉTODOS

letters = [ 
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!','#','$','%','&','*','(',')','+']

print("Welcome to the Pypassword Generator!")
num_letters = int(input("How many letters would tou like in your password? "))
num_numbers = int(input("How many numbers would tou like in your password? "))
num_symbols = int(input("How many symbols would tou like in your password? "))

letters_list = []
for i in range (0, num_letters):
    letters_list.append(letters[random.randint(0, len(letters)-1)])

numbers_list = []
for i in range (0, num_numbers):
    numbers_list.append(numbers[random.randint(0, len(numbers)-1)])

symbols_list = []
for i in range (0, num_symbols):
    symbols_list.append(symbols[random.randint(0, len(symbols)-1)])

print(letters_list)
print(numbers_list)
print(symbols_list)

letters_times = 0
numbers_times = 0
symbols_times = 0
password = ""

for i in range (0, (num_letters+num_numbers+num_symbols)):
    item = random.randint(1, 3)

    if item == 1 and letters_times == num_letters:
        item = 2

    if item == 2 and numbers_times!= num_numbers:
        password += numbers_list[numbers_times]
        numbers_times+=1

    if item == 2 and numbers_times == num_numbers:
        item = 3

    if item == 3 and symbols_times!= num_symbols:
        password += symbols_list[symbols_times]
        symbols_times+=1

    if item == 3 and symbols_times == num_symbols:
        item = 1

    if item == 1 and letters_times!= num_letters:
        password += letters_list[letters_times]
        letters_times+=1
    

    

print(f"Your password is: {password}")