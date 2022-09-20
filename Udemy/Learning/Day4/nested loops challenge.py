travel_log = [
    {
        "country": "France",
        "times visited": 12,
        "cities visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "times visited": 5,
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(name, visit_count, cities_visited):
    new_country = {}
    new_country["country"] = name
    new_country["time visited"] = visit_count
    new_country["cities visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
