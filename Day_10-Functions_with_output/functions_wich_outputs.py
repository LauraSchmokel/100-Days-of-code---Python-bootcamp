# Day 10 - Functions with Return Values (Exercise: Name Formatter)
# Topics: return statements, f-strings, .title() method
# What I learned: how functions can return values to be used in other parts of the code

def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

titled_name = format_name(f_name=f_name, l_name=l_name)

print(titled_name)

