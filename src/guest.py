

class Guest:
    
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = fav_song
        
    def pay_entry_fee(self, amount):
        if self.check_sufficient_funds(amount):
            self.wallet -= amount
        return amount

    def check_sufficient_funds(self, item):
        return self.wallet >= item

