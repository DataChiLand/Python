
from replit import clear

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bidding_record = {"Anglea": 123, "James": 321}
    for bidder in bidding_record:
        big_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    print(f"The winner is {winner} with the bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[names] = price
    input("Are there any other bidders? Type 'yes or no'. ")
    if should_continue == "no":
        bidding_finshed = True
    elif should_continue == "yes":
        clear()