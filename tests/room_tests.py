import  unittest

from src.guest import Guest
from src.room import Room
from src.song import Song


class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.rich_guest = Guest("Pheobe", 70.00, "Dancing Queen", "Wiggle", True)
        self.poor_guest = Guest("Chandler", 4.00, "Sweet Caroline", "Hip-Shake", False)
        self.guest = Guest("Monica", 40.00, "I Will Survive", "The Worm", True)

        self.song = { 
            "Dancing Queen": Song("Dancing Queen", "ABBA"),
            "I Will Survive": Song("I Will Survive", "Gloria Gaynor"),
            "Sweet Caroline": Song("Sweet Caroline", "Neil Diamond")
        }

        self.vip_room = Room("Super Stars", 100.00, 2, 5.00, self.song)
        self.non_vip_room = Room("Screechers", 100.00, 3, 2.00, self.song)




    def test_room_has_a_name(self):
        self.assertEqual("Super Stars", self.vip_room.name)

    def test_room_has_money_in_till(self):
        self.assertEqual(100.00, self.vip_room.till)

    def test_room_has_empty_guest_list(self):
        self.assertEqual([], self.vip_room.guest_list)

    def test_room_has_empty_playlist(self):
         self.assertEqual([], self.vip_room.playlist)

    def test_guest_room_limit_set(self):
        self.assertEqual(2, self.vip_room.room_limit)

    def test_room_has_space_returns_True_when_room_has_space(self):
        self.assertEqual(True, self.vip_room.check_room_has_space(self.vip_room))
    
    def test_room_has_space_returns_False_when_room_is_full(self):
        self.vip_room.admit_guest(self.rich_guest, self.vip_room, self.non_vip_room)
        self.vip_room.admit_guest(self.rich_guest, self.vip_room, self.non_vip_room)
        self.vip_room.admit_guest(self.rich_guest, self.vip_room, self.non_vip_room)
        self.assertEqual(False, self.vip_room.check_room_has_space(self.vip_room))

    def test_guest_admitted_when_room_has_space_and_enough_money(self):
        self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.assertEqual(1, len(self.non_vip_room.guest_list))

    def test_guest_not_admitted_when_room_has_space_but_not_enough_money(self):
        self.assertEqual("Sorry, you are not getting in tonight.", self.vip_room.admit_guest(self.poor_guest, self.non_vip_room, self.vip_room))    

    
    
    # This test passes however is wrong as it passes a VIP guest into a non-vip Room
    def test_guest_not_admitted_when_has_enough_money_but_capacity_full(self):
        self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.assertEqual(3, len(self.non_vip_room.guest_list))
        self.assertEqual("Sorry, you are not getting in tonight.",self.non_vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room))


    def test_remove_guest_from_guest_list(self):
        self.vip_room.admit_guest(self.guest, self.non_vip_room, self.vip_room)
        self.vip_room.remove_guest(self.guest, self.non_vip_room)
        self.assertEqual(0, len(self.non_vip_room.guest_list))

    def test_money_can_be_added_to_till(self):
        self.vip_room.add_money_to_till(self.vip_room.entry_fee)
        self.assertEqual(105.00, self.vip_room.till)

    def test_get_guest_fav_song(self):
        self.assertEqual("I Will Survive", self.vip_room.get_guest_favourite_song(self.guest))
        
    def test_add_favourite_song_to_playlist(self):
        self.vip_room.add_favourite_song_to_playlist(self.guest)
        self.assertEqual(1, len(self.vip_room.playlist))

    # def test_remove_song_from_playlist(self):
    #     self.room.add_favourite_song_to_playlist(self.guest, self.song)
    #     self.room.remove_guest_song_from_playlist(self.guest)
    #     self.assertEqual(0, len(self.room.playlist))

    def test_play_song_from_playlist(self):
        self.vip_room.add_favourite_song_to_playlist(self.guest)
        self.assertEqual(self.song["I Will Survive"] , self.vip_room.play_song_from_playlist())

    def test_guest_cheers_when_fav_song_is_played(self):
        self.vip_room.admit_guest(self.rich_guest, self.non_vip_room, self.vip_room)
        self.vip_room.admit_guest(self.rich_guest, self.non_vip_room, self.vip_room)
        self.vip_room.admit_guest(self.rich_guest, self.non_vip_room, self.vip_room)
        self.assertEqual("Woo, that's my tune!" and self.rich_guest.dance_moves, self.vip_room.guest_cheers_and_dances())

