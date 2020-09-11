from src.song import Song
from src.guest import Guest


class Room:

    def __init__(self, name, till, room_limit, entry_fee):
        self.name = name
        self.till = till
        self.guest_list = []
        self.playlist = {}
        self.room_limit = room_limit
        self.entry_fee = entry_fee

    def admit_guest(self, guest):
        if self.check_room_limit:
            self.guest_list.append(guest)
            guest.pay_entry_fee(self.entry_fee)
        else:
            return "Sorry the room is currently full."

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)

    def check_room_limit(self):
        if len(self.guest_list) < self.room_limit:
            return True
        else:
            return False
        
    def add_money_to_till(self, amount):
        self.till += amount

    def get_guest_favourite_song(self,guest):
        return guest.favourite_song
        
    # def add_favourite_song_to_playlist(self, guest):
    #     fav_song = self.get_guest_favourite_song(guest)
    #     if fav_song == 

    
