

class Guest:
    
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = fav_song
        
    def pay_entry_fee(self, amount):
        if self.has_sufficient_funds(amount):
            self.wallet -= amount


    def has_sufficient_funds(self, item):
        return self.wallet >= item

    def cheer_for_fav_song(self):
        return "Woo, that's my tune!"