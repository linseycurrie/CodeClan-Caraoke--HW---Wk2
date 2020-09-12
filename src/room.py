import random
from src.song import Song
from src.guest import Guest



class Room:

    def __init__(self, name, till, room_limit, entry_fee):
        self.name = name
        self.till = till
        self.guest_list = []
        self.playlist = []
        self.room_limit = room_limit
        self.entry_fee = entry_fee

    def admit_guest(self, guest, songs):
        if (self.check_if_guest_can_be_admitted(guest) == True):
            self.guest_list.append(guest)
            guest.pay_entry_fee(self.entry_fee)
            self.add_money_to_till(self.entry_fee)
            self.add_favourite_song_to_playlist(guest, songs)
        else:
            return "Sorry the room is currently full."

    def remove_guest(self, guest):
        if guest in self.guest_list:
            self.guest_list.remove(guest)
    
    def check_if_guest_can_be_admitted(self, guest):
        if (self.check_room_has_space() == True) and (guest.has_sufficient_funds(self.entry_fee) == True):
            return True

    def get_size_of_guest_list(self):
        return len(self.guest_list)
            

    def check_room_has_space(self):
        if self.get_size_of_guest_list() < self.room_limit:
            return True
        else:
            return False
        
    def add_money_to_till(self, amount):
        self.till += amount

    def get_guest_favourite_song(self,guest):
        return guest.favourite_song
        
    def add_favourite_song_to_playlist(self, guest, songs):
        fav_song = self.get_guest_favourite_song(guest)
        if fav_song in songs.keys():
            song_to_add = songs.get(str(fav_song))
            self.playlist.append(song_to_add)

    # def remove_guest_song_from_playlist(self, guest):
    #     song_name = self.get_guest_favourite_song(guest)
    #     print(self.playlist)
    #     self.playlist.index(str(song_name))
    #     print(song_name)
    #     self.playlist.remove(song_name)

    def play_song_from_playlist(self):
        random_index = random.choice(range(len(self.playlist)))
        return self.playlist[random_index]

    def guest_cheers(self, songs):
        for guest in self.guest_list:
            song_name = guest.favourite_song
            if self.play_song_from_playlist() == songs[str(song_name)]:
                return guest.cheer_for_fav_song()

    
