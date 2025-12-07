def life_in_weeks(age):
    print(f"You have {(90 * 52) - (age * 52)} weeks left!")

age = int(input("How old are you? "))
life_in_weeks(age)