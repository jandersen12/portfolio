## Online Second-Price Ad Auction Simulation

### Overview
This Python simulation models an online second-price ad auction, where multiple bidders compete to show ads to users with hidden click probabilities. Over multiple rounds, bidders adjust their strategies to maximize profits.

### How It Works
Users each have a secret click probability.

Bidders try to bid wisely based on how likely users are to click.

Auction rounds simulate ad placements using second-price auction rules:

- Highest bidder wins

- Winner pays the second-highest bid

- If the ad is clicked, the winner gets $1

### Tools
This projects applies key concepts from Object-Oriented Programming in Python such as encapsulation, inheritance and polymorphism. Creating classes that encapsulate their own attributes and methods helps the code to be modular and adaptable. The code can also be reused and extended due to child classes inheriting behaviors from parent classes. Polymorphism is incorporated through bidders applying different strategies within the same auction framework. 

Not only did this project provide insight and clarity into the mechanics of strategic bidding and auction theory, but also taught me the importance of designing systems that are flexible, maintainable, and easily modified. 

### File Overview
auction_and_users.py: Defines the User and Auction classes.

bidder_source_code.py: Implements the Bidder class and bidding logic.

execute_auction.py: Runs the simulation with multiple users, bidders, and rounds.

