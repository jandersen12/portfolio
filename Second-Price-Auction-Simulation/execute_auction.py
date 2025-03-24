'''
Creates lists of users and bidders to participate in the auction.

Executes the auction and prints the final winnings for each bidder.
'''

from auction_rounds import Auction
from auction_rounds import User
from bidder_source_code import Bidder

# Create a list of User objects
users_list = [User() for _ in range(5)]

# Create a list of Bidder objects
# For example, each bidder knows there are 5 users and 10 rounds in total
bidders_list = [Bidder(num_users=5, num_rounds=10) for _ in range(3)]

# Initialize the Auction with the lists of users and bidders
auction = Auction(users_list, bidders_list)

# Run the auction for a specific number of rounds
num_rounds = 10
for round_number in range(num_rounds):
    auction.execute_round()

# Print final balances of each bidder
print("\nFinal balances of each bidder:")
for bidder_id, balance in auction.balances.items():
    print(f"Bidder {bidder_id}: ${balance:.2f}")
