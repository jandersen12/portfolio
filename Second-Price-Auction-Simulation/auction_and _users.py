import numpy as np
# import bidder_andersen as Bidder

class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        
        # Generates the user's hidden random probability between 0 and 1
        self.__probability = np.random.rand() 

    def __repr__(self):
        '''User object with secret probability'''
        
        return f'{self.__probability}' 

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        
        return self.__repr__()

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
       
       # Generates a random number between 0 and 1 and compares it with the user probability to see if they clicked.
        clicked = np.random.binomial(1, self.__probability) 
        return bool(clicked)

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''

        # Create a dictionary of users with user IDs
        self.users = {user_id: user for user_id, user in enumerate(users)}  

        # Create a dictionary of bidders with bidder IDs
        self.bidders = {bidder_id: bidder for bidder_id, bidder in enumerate(bidders)}

        # Initialize balances dictionary for each bidder
        self.balances = {bidder_id: 0 for bidder_id in self.bidders}

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return (f'List of users: {list(self.users.keys())} \n'
                f'List of bidders and their balances: {self.balances}')

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return self.__repr__()

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection 
            - bids from every qualified bidder in the auction 
            - selection of winning bidder based on maximum bid 
            - selection of actual price (second-highest bid) 
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome
            - notifying losing bidders of price
            - updating all bidder balances'''
        
        # Step 1: Random user selection
        chosen_user_id = np.random.choice(list(self.users.keys()))

        # Step 2: bids from every qualified bidder in the auction
        self.bids = {}
        for bidder_id, bidder in self.bidders.items():
            if self.balances[bidder_id] > -1000:
                self.bids[bidder_id] = bidder.bid(chosen_user_id)
            else:
                self.bids[bidder_id] = 0
        
        # Step 3: Selection of winning bidder based on maximum bid and selection of actual price (second-highest bid)
        sorted_bids = sorted(self.bids.items(), key=lambda x: x[1], reverse=True)
        
        if len(sorted_bids) > 1:
            winning_bidder_id, highest_bid = sorted_bids[0]  # Highest bid
            second_highest_bid = sorted_bids[1][1]  # Second-highest bid
        else:
            winning_bidder_id, highest_bid = sorted_bids[0]
            second_highest_bid = 0

        # Step 4: Showing ad to user and finding out whether or not they click
        user_clicked = self.users[chosen_user_id].show_ad()

        # Step 5: Notify the winning and losing bidders and update their balances with the notify method
        winning_bidder = self.bidders[winning_bidder_id]
        winning_bidder.notify(auction_winner=True, price=second_highest_bid, clicked=user_clicked)

        for bidder_id in self.bidders:
            if bidder_id != winning_bidder_id:
                self.bidders[bidder_id].notify(auction_winner=False, price=second_highest_bid, clicked=None)

        # Step 6: Adjust the winning bidder balance
        self.balances[winning_bidder_id] -= second_highest_bid
        if user_clicked:
            self.balances[winning_bidder_id] += 1
        self.balances[winning_bidder_id] = round(self.balances[winning_bidder_id], 2)