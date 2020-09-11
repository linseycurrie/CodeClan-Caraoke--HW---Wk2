import  unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Don't Stop Believin'", "Journey")

    def test_song_has_name(self):
        self.assertEqual("Don't Stop Believin'", self.song.name)
    
    def test_song_has_artist(self):
        self.assertEqual("Journey", self.song.artist)