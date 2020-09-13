import random
from src.song import Song
from src.guest import Guest



class Room:

    def __init__(self, name, till, room_limit, entry_fee, song_list):
        self.name = name
        self.till = till
        self.guest_list = []
        self.playlist = []
        self.room_limit = room_limit
        self.entry_fee = entry_fee
        self.song_list = song_list



    def admit_guest(self, guest, vip_room, non_vip_room):
        # import pdb; pdb.set_trace()
        if (self.do_you_have_VIP_status(guest) == True):
            if (self.check_if_guest_can_be_admitted(guest, vip_room)):
                self.pay_entry_fee(guest, vip_room)
                vip_room.admit_guest_and_add_song_to_playlist(guest, vip_room)
            else:
                return "Sorry, you are not getting in tonight."   
        elif(self.do_you_have_VIP_status(guest) == False): 
            if (self.check_if_guest_can_be_admitted(guest, non_vip_room) == True):
                self.pay_entry_fee(guest, non_vip_room)
                non_vip_room.admit_guest_and_add_song_to_playlist(guest, non_vip_room)
            else:
                return "Sorry, you are not getting in tonight."

    def pay_entry_fee(self, guest, room):
        guest.pay_entry_fee(room.entry_fee)
        room.add_money_to_till(room.entry_fee)

    def admit_guest_and_add_song_to_playlist(self, guest, room):
        room.guest_list.append(guest)
        room.add_favourite_song_to_playlist(guest)


    
    def do_you_have_VIP_status(self, guest):
        if guest.vip_status == True:
            return True
        else:
            return False
    
    def check_if_guest_can_be_admitted(self, guest, room):
        if (guest.has_sufficient_funds(room.entry_fee) == True) and (self.check_room_has_space(room) == True):
            return True
        else:
            return False

    def check_room_has_space(self, room):
        if len(room.guest_list) < room.room_limit:
            return True
        else:
            return False
        
    def add_money_to_till(self, amount):
        self.till += amount
    
    def remove_guest(self, guest, room):
        if guest in room.guest_list:
            room.guest_list.remove(guest)


    def get_guest_favourite_song(self, guest):
        return guest.favourite_song
        
    def add_favourite_song_to_playlist(self, guest):
        fav_song = self.get_guest_favourite_song(guest)
        if fav_song in self.song_list.keys():
            song_to_add = self.song_list.get(str(fav_song))
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

    def guest_cheers_and_dances(self):
        for guest in self.guest_list:
            song_name = guest.favourite_song
            if self.play_song_from_playlist() == self.song_list[str(song_name)]:
                return guest.cheer_for_fav_song() and guest.show_off_dance_moves()


        
        