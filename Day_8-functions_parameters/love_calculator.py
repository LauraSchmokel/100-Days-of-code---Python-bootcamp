# Day 8 - Functions with Parameters (Exercise: Love Calculator)
# Topics: counting characters in strings, conditional logic inside functions
# What I learned: how to manipulate strings inside a function to extract specific information

def calculate_love_score(name1, name2):
    true_times = 0
    love_times = 0

    for letter in "true":
        for name_letter in name1.lower():
            if letter == name_letter:
                true_times += 1

        for name_letter in name2.lower():
            if letter == name_letter:
                true_times += 1

    for letter in "love":
        for name_letter in name1.lower():
            if letter == name_letter:
                love_times += 1

        for name_letter in name2.lower():
            if letter == name_letter:
                love_times += 1

    print(f"Love score: {str(true_times)+str(love_times)}!")



name1 = input("First name: ")
name2 = input("Second name: ")

calculate_love_score(name1=name1, name2=name2)
