import random
from Games.Day9.game_data import data
from Games.Day9.art import logo
from Games.Day9.art import vs

# loop:
game_end = False

# score
score = 0


def get_random_person(random_person_1, random_person_2):
    original_person_2 = random_person2
    while random_person_1 == random_person_2 or original_person_2 == random_person_2:
        random_person_2 = random.choice(data)

    return [random_person_2, random_person_1]
# continue with 29/09/22
# currently 11:23pm


"""Takes the account data and return a printable format of code."""
# formatting 1:
account_name1 = random_person1["name"]
account_followers1 = random_person1["follower_count"]  # remove these from printer at first
account_description1 = random_person1["description"]
account_country1 = random_person1["country"]
# formatting2:
account_name2 = random_person2["name"]
account_followers2 = random_person2["follower_count"]
account_description2 = random_person2["description"]
account_country2 = random_person2["country"]


def start():
    # higher or lower logo:
    print(logo)
    # where the first option goes:
    print(f"Compare A: {account_name1}, a {account_description1}, from {account_country1}")
    # vs sign:
    print(vs)
    # where the second option goes:
    print(f"Against B: {account_name2}, a {account_description2}, from {account_country2}")


random_person2 = random.choice(data)

while not game_end:
    def main():
        global random_person1
        global random_person2
        random_person1 = random_person2
        random_person2 = random.choice(data)

        # globals:
        global score
        global game_end
        start()
        print(f"Your current score is {score}")

        # the users guess:
        guess = input("Who has more followers? Type 'A' or 'B':\n").upper()
        if guess == "A":
            if account_followers1 > account_followers2:
                score += 1
                print(f"You're correct! Your score is: {score}")
            elif account_followers1 < account_followers2:
                print(f"Sorry you were wrong. Your final score was {score}")
                game_end = True
        elif guess == "B":
            if account_followers2 > account_followers1:
                score += 1
                print(f"You're correct! Your score is: {score}")
            elif account_followers2 < account_followers1:
                print(f"Sorry you were wrong. Your final score was {score}")
                game_end = True


    main()

# make it offer knew people but with the correct answer from the previous question []
