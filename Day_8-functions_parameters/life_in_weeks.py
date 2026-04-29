# Day 8 - Functions with Parameters (Exercise: Life in Weeks)
# Topics: function parameters, mathematical calculations inside functions
# What I learned: how to wrap calculations in a function and reuse them with different inputs

def life_in_weeks(age):
    print(f"You have {(90 * 52) - (age * 52)} weeks left!")

age = int(input("How old are you? "))
life_in_weeks(age)