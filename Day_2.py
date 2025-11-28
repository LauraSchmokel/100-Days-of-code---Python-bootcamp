
# print("Hello"[-3])

# print(type(True))
# print(type("Laura"))
# print(type(12345))
# print(type(3.1415)) 

# num = "123"
# num = int(num)

# print(type(num)) 

# username = input("Entre your name: ")
# length_name = len(username)

# print("Number of letters in your name:", str(length_name))

# print(round(7/2)) 

# score = 0
# score =+ 1

# print(f"Your score is: {score}" )

#CHALLENGE

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))

tip = total_bill * (tip/100)

payment = (total_bill + tip)/total_people

payment = round(payment, 2)


print(f"Each person should pay: {payment}")

