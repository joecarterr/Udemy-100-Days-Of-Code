capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary
travel_log = [
    # FRANCE
    {
        "country": "France",
        "cities_visited_france": ['Paris', "Lille", "Dijon"],
        "total_visits_france": 6,
    },
    # GERMANY
    {
        "country": "Germany",
        "cities_visited_germany": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits_germany": 10,
    },
]

# you can index the item you want in a dictionary like this: e.g. [0], [1], [2], ect
print(travel_log[0])
print(travel_log[1])
