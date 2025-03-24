class Bidder:
    '''Class to represent a bidder in an online second-price ad auction'''

    def __init__(self, num_users, num_rounds):
        '''Setting number of users, number of rounds, and round counter'''
        
        # Set the number of users and number of rounds
        self.num_users = num_users
        self.num_rounds = num_rounds
        
        # Set the bidder balance and neutral beginning click probability estimate
        self.bidder_balance = 0
        self.click_probability = 0.5 
        self.round_count = 0

        # Track the last user_id that was selected
        self.last_user_id = None

    def __repr__(self):
       '''Return a representation of the Bidder object'''
       return f"Bidder(bidder balance= {self.bidder_balance}, number of users= {self.num_users}, number of rounds= {self.num_rounds}, round count={self.round_count})"

    def __str__(self):
        '''Return Bidder object'''
        return self.__repr__()
    
    def get_balance(self):
        '''Return the current balance of the bidder.'''
        return self.bidder_balance

    def bid(self, user_id):
        '''Returns a non-negative bid amount based on estimated click probability'''

        # Store the last user_id this bid was made for
        self.last_user_id = user_id

        # Use the general click probability to determine bid amount
        if self.click_probability >= 0.8:
            bid_amount = 0.99  # High probability, high bid
        elif 0.5 < self.click_probability < 0.8:
            bid_amount = self.click_probability * 0.75  # Medium probability, medium bid
        elif 0.3 < self.click_probability <= 0.5:
            bid_amount = self.click_probability * 0.3  # Low probability, lower bid
        else:
            bid_amount = 0.1  # Very low probability, minimal bid
        
        return round(bid_amount, 2)

    def notify(self, auction_winner, price, clicked = None):
        '''Updates bidder attributes based on results from an auction round'''
        
        # Increase the round count by 1 once the round is finished
        self.round_count += 1

        if auction_winner:
            # Subtract the second-highest bid price from balance
            self.bidder_balance -= price  

            if clicked:
                # $1 reward if the ad was clicked
                self.bidder_balance += 1 

            # Update the click probability estimate
            previous_estimate = self.click_probability
            updated_estimate = (previous_estimate * (self.round_count - 1) + (1 if clicked else 0)) / self.round_count
            self.click_probability = updated_estimate