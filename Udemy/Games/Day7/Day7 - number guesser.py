from Games.Day7.art import logo
import random

print(logo)

# LOOP:
again = True

# WELCOME:
answer = random.randint(1, 100)
print(f"""Welcome to the number guesser game!
I'm thinking of a number between 1 and 100.
Psst. The correct answer is {answer}""")
difficulty = input(f"Please enter 'easy' for easy difficulty and 'hard' for more of a challenge:\n").lower()

global lives
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
while again:
    user_won = False
    global user_guess
    # EASY MODE:
    if difficulty == "easy":
        user_guess = int(input("Please enter a guess between 1 and 100:\n"))
        # INCORRECT ANSWER:
        if user_guess != answer:
            lives -= 1
            print(f"Sorry, that is the incorrect guess you have {lives} remaining")
        # CORRECT ANSWER:
        elif user_guess == answer:
            print(f"Welcome {answer} was the correct guess!")
            user_won = True
            quit()

    # HARD MODE:
    elif difficulty == "hard":
        lives = 5
        user_guess = int(input("Please enter a guess between 1 and 100:\n"))
        # INCORRECT ANSWER:
        if user_guess != answer:
            lives -= 1
            print(f"Sorry, that is the incorrect guess you have {lives} remaining")
        # CORRECT ANSWER:
        elif user_guess == answer:
            print(f"Welcome {answer} was the correct guess!")
            user_won = True
            quit()
        elif user_guess < answer:
            print("""Too low
            Make another guess""")
            lives -= 1
            print(f"You have {lives} chances remaining")
        elif user_guess > answer:
            print("""Too large
            Make another guess""")
            lives -= 1
            print(f"You have {lives} chances left")
        if lives == 0 and not user_won:
            print("Sorry you ran out of lives")

    # USER ERRORS:
    if user_guess > 100:
        print("\nSorry this is an invalid option")
        quit()

    if lives <= 0:
        print("You ran out of lives :(")
        quit()
