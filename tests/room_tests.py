import  unittest

from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song = { 
            "Dancing Queen": Song("Dancing Queen", "ABBA"),
            "I Will Survive": Song("I Will Survive", "Gloria Gaynor"),
            "Sweet Caroline": Song("Sweet Caroline", "Neil Diamond")
        }
        self.room = Room("Super Stars", 100.00, 2, 5.00, self.song)
        self.guest = Guest("Monica", 40.00, "I Will Survive", "The Worm", "non-VIP")
        self.rich_guest = Guest("Pheobe", 70.00, "Dancing Queen", "Wiggle", "VIP")
        self.poor_guest = Guest("Chandler", 4.00, "Sweet Caroline", "Hip-Shake", "non-VIP")


    def test_room_has_a_name(self):
        self.assertEqual("Super Stars", self.room.name)

    def test_room_has_money_in_till(self):
        self.assertEqual(100.00, self.room.till)

    def test_room_has_empty_guest_list(self):
        self.assertEqual([], self.room.guest_list)

    def test_room_has_empty_playlist(self):
         self.assertEqual([], self.room.playlist)

    def test_guest_room_limit_set(self):
        self.assertEqual(2, self.room.room_limit)

    def test_room_has_space_returns_True_when_room_has_space(self):
        self.assertEqual(True, self.room.check_room_has_space())
    
    def test_room_has_space_returns_False_when_room_is_full(self):
        self.room.admit_guest(self.guest)
        self.room.admit_guest(self.rich_guest)
        self.room.admit_guest(self.rich_guest)
        self.assertEqual(False, self.room.check_room_has_space())

    def test_guest_admitted_when_room_has_space_and_enough_money(self):
        self.room.admit_guest(self.guest)
        self.assertEqual(1, len(self.room.guest_list))

    def test_guest_not_admitted_when_room_has_space_but_not_enough_money(self):
        self.assertEqual("Sorry the room is currently full.", self.room.admit_guest(self.poor_guest))    

    def test_guest_not_admitted_when_has_enough_money_but_capacity_full(self):
        self.room.admit_guest(self.guest)
        self.room.admit_guest(self.rich_guest)
        self.assertEqual("Sorry the room is currently full.",self.room.admit_guest(self.guest))
        self.assertEqual(2, len(self.room.guest_list))

    def test_remove_guest_from_guest_list(self):
        self.room.admit_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guest_list))

    def test_money_can_be_added_to_till(self):
        self.room.add_money_to_till(self.room.entry_fee)
        self.assertEqual(105.00, self.room.till)

    def test_get_guest_fav_song(self):
        self.assertEqual("I Will Survive", self.room.get_guest_favourite_song(self.guest))
        
    def test_add_favourite_song_to_playlist(self):
        self.room.add_favourite_song_to_playlist(self.guest)
        self.assertEqual(1, len(self.room.playlist))

    # def test_remove_song_from_playlist(self):
    #     self.room.add_favourite_song_to_playlist(self.guest, self.song)
    #     self.room.remove_guest_song_from_playlist(self.guest)
    #     self.assertEqual(0, len(self.room.playlist))

    def test_play_song_from_playlist(self):
        self.room.add_favourite_song_to_playlist(self.guest)
        self.assertEqual(self.song["I Will Survive"] , self.room.play_song_from_playlist())

    def test_guest_cheers_when_fav_song_is_played(self):
        self.room.admit_guest(self.guest)
        self.room.admit_guest(self.rich_guest)
        self.room.admit_guest(self.poor_guest)
        self.assertEqual("Woo, that's my tune!" and self.guest.dance_moves, self.room.guest_cheers())