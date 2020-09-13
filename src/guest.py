
class Guest:
    
    def __init__(self, name, wallet, fav_song, dance_moves, vip_status):
        self.name = name
        self.wallet = wallet
        self.favourite_song = fav_song
        self.dance_moves = dance_moves
        self.vip_status = vip_status
        
    def pay_entry_fee(self, amount):
        if self.has_sufficient_funds(amount):
            self.wallet -= amount


    def has_sufficient_funds(self, item):
        return self.wallet >= item

    def cheer_for_fav_song(self):
        return "Woo, that's my tune!"

    def show_off_dance_moves(self):
        return self.dance_moves