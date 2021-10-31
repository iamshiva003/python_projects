import os
from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder (bidding_record):
    highest_bid = 0
    # bidding_record = {"Shivu" : 123, "James" : 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    os.system('cls')
    print (f"The Winner is {winner} with a bid of ${highest_bid}")
    print ()

while not bidding_finished:
    name  = input("What is your name? : ") 
    price = int(input("What is your price? : $"))
    bids[name] = price
    should_continue = input("Are therer any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
        
