# imports:
import random
from MainProjects.Blackjack.art import logo
import time

# blackjack game logo:
print(logo)

# loop:
game_continue = True


# random card selector:
def deal_cards():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(card_list)
    return random_card


# playing the main blackjack game:
def play():
    bet_amount = int(input("Please enter the amount you'd like to £"))
    user_cards = [deal_cards(), deal_cards()]
    dealer_cards = [deal_cards(), deal_cards()]
    user_total = calculating_scores(user_cards)
    print(f"You got the cards: {user_cards}, giving you a total of {user_total}\n")
    print(f"The dealer's first card: {dealer_cards[0]}\n")

    # user blackjack:
    if user_total == 21:
        print("You won! You had BLACKJACK!!!")
        bet_amount *= 2.5
        print(f"You won {bet_amount}")
        quit()

    # while the user has anything less than blackjack:
    while user_total < 21:
        another_card = input("Type 'y' if you'd like another card:\n")
        if another_card == "yes" or another_card == "y":
            # adding a card to the total card user list:
            user_cards.append(deal_cards())
            user_total = calculating_scores(user_cards)
            print(f"\nYou have the cards, {user_cards}, giving you a total of: {user_total}")
        else:
            break
    dealer_total = calculating_scores(dealer_cards)
    print(f"The dealers second card was {dealer_cards[-1]}, giving him a total of {dealer_total}")
    time.sleep(.3)

    # if the dealers score is below 17 then they will take another card:
    while dealer_total <= 17:
        print("\nThe dealer takes another card\n")
        dealer_cards.append(deal_cards())
        dealer_total = calculating_scores(dealer_cards)
        print(f"The dealers next card was {dealer_cards[-1]}, giving him a total of {dealer_total}\n")

    # dealer blackjack:
    if dealer_total == 21:
        print("You lost. The dealer had blackjack :(")
        print(f"You lost £{bet_amount}")
        quit()

    # user blackjack:
    elif user_total == 21:
        print("You won! You had BLACKJACK!!!")
        bet_amount *= 2.5
        print(f"You won £{bet_amount}")
        quit()

    # user loss:
    if user_total > 21:
        print("\nYou went bust, dealer wins!\n")
        print(f"You lost £{bet_amount}")
        quit()

    # user win
    elif dealer_total > 21:
        print("\nYou win! The dealer went bust!\n")
        bet_amount *= 2
        print(f"You won £{bet_amount}")
        quit()

    # who won the game
    if user_total > dealer_total:
        print(f"\nYou win you had a score of {user_total}. The dealer had a score of {dealer_total}\n")
        quit()

    elif user_total < dealer_total:
        print(f"\nYou lost. You had a score of {user_total} and the dealer had a score of {dealer_total}\n")
        quit()

    elif user_total == dealer_total:
        print(f"\nIt was a draw you both scored {user_total}\n")
        quit() 

    return user_total, dealer_total


# if someone got an ace but then goes over 21 the ace is changed to a value of one instead of 11. Giving them another
# shot at winning:
def calculating_scores(card_list):
    while 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


start = input("Type 'y' if you'd like to start:\n").lower()
if start == "y":

    if start == "y" or start == "yes":
        play()
    else:
        print("Okay, thank you!")
        quit()
