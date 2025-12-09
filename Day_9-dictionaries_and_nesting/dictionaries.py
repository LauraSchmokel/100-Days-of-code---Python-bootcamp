# colours = {
#     "apple": "red",
#     "pear": "green",
#     "banana": "yellow"
# }

# print(colours["apple"])

# colours["orange"] = "orange"
# print(colours)

# new_dictionary = {}

# colours = {}
# print(colours)

# colours["apple"] = "green"
# print(colours)

# for key in colours:
#     print(key)
#     print(colours[key])

# -----------------------------------------------

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["D", "E"]]

# print(nested_list[2][0])
travel_log = { 
    "France": {
        "num_times_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": [ "Berlin", "Hamburg", "Stuttgart",]
        
    }
}

print(travel_log["Germany"]["cities_visited"][2])