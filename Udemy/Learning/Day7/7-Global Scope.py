# global scope (available at any point of the file because it's not within another function)
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        # outputs 2:
        print(potion_strength)
        # outputs 10 even though it is not in the function:
        print(f"Player's health is {player_health}")

    # function has to be in the location of what's being called as it is local:
    drink_potion()
