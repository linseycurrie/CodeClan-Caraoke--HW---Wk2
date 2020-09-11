import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room = Room("Super Stars", 100.00, 2, 5.00)
        self.guest = Guest("Joey", 50.00, "Don't Stop Believin'")


    def test_guest_has_name(self):
        self.assertEqual("Joey", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(50.00, self.guest.wallet)
    
    def test_guest_has_favourite_Song(self):
        self.assertEqual("Don't Stop Believin'", self.guest.favourite_song)
    
    def test_can_pay_entry_fee_sufficient_funds(self):
        value = self.room.entry_fee
        self.guest.pay_entry_fee(value)
        self.assertEqual(45.00, self.guest.wallet)
    
    