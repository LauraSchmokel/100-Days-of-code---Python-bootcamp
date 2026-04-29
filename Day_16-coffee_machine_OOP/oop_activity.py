# Day 16 - Introduction to OOP (Object-Oriented Programming)
# Topics: OOP concepts, turtle library, PrettyTable library, instances and attributes
# What I learned: the fundamentals of object-oriented programming and how to use external libraries

from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)

# my_screen = Screen()
# # print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Charmander", "Squirtle", "Bulbasaur"])
table.add_column("Pokemon Type", ["Fire", "Water", "Plant"])

# table.field_names = ["Pokemon Name", "Pokemon Type"]
# table.add_row(["Charmander", "Fire"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Bulbasaur", "Plant"])

table.align = "l"

print(table)