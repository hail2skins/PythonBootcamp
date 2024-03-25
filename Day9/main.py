# Blind auction program
# Show the logo from the art.py file.
from art import logo
print(logo)

# Print welcome message
print("Welcome to the secret auction program.")

# Declare an empty dictionary to store the bids
bids = {}
bidding_finished = False # Flag to check if the bidding is finished

# function to find the highest bidder
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Loop through the bidders
while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    # Check if there are other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    # Condition to check if the bidding is finished
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\033c") # Clear console

