## Online Second-Price Ad Auction Simulation

This Python simulation models an online second-price ad auction, where multiple bidders compete to show ads to users with hidden click probabilities. Over multiple rounds, bidders adjust their strategies to maximize profits.

### How It Works
Users each have a secret click probability.

Bidders try to bid wisely based on how likely users are to click.

Auction rounds simulate ad placements using second-price auction rules:

- Highest bidder wins

- Winner pays the second-highest bid

- If the ad is clicked, the winner gets $1

### File Overview
auction_and_users.py: Defines the User and Auction classes.

bidder_source_code.py: Implements the Bidder class and bidding logic.

execute_auction.py: Runs the simulation with multiple users, bidders, and rounds.

