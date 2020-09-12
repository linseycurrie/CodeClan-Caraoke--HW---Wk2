import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song = { 
            "Dancing Queen": Song("Dancing Queen", "ABBA"),
            "I Will Survive": Song("I Will Survive", "Gloria Gaynor"),
            "Sweet Caroline": Song("Sweet Caroline", "Neil Diamond")
        }
        self.vip_room = Room("Super Stars", 100.00, 2, 5.00, self.song)
        self.non_vip_room = Room("Screechers", 100.00, 3, 2.00, self.song)
        self.guest = Guest("Joey", 50.00, "Don't Stop Believin'", "The Floss", "non-VIP")
        self.vip_guest = Guest("Ross", 30.00, "Sweet Caroline", "Moonwalk", "VIP")



    def test_guest_has_name(self):
        self.assertEqual("Joey", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(50.00, self.guest.wallet)
    
    def test_guest_has_favourite_Song(self):
        self.assertEqual("Don't Stop Believin'", self.guest.favourite_song)
    
    def test_can_pay_entry_fee_sufficient_funds(self):
        value = self.vip_room.entry_fee
        self.guest.pay_entry_fee(value)
        self.assertEqual(45.00, self.guest.wallet)
    
    