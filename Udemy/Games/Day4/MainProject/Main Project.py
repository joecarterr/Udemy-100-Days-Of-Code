from replit import clear
from Games.Day4.MainProject import art

again = True

bids = {}
bidding_finished = False

print(art.logo)
print("Welcome to the secret auction program")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"{winner} had the highest bid of £{highest_bid}")
    quit()


while not bidding_finished:
    user_name = input("What's your name?:\n")
    user_bid = int(input("What's your bid?: £"))
    bids[user_name] = user_bid
    other_bidders = input("Are there any other bidders?:\n").lower()
    if other_bidders == "yes" or other_bidders == "y":
        clear()
    elif other_bidders == "no" or other_bidders == "n":
        find_highest_bidder(bids)
    else:
        bidding_finished = True
