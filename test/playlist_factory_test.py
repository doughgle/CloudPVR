'''
Created on May 30, 2013

@author: dough
'''
import unittest
from mock import MagicMock
from playlist_factory import PlaylistFactory
from playlist import Playlist
from time import time

class TestPlaylistFactory(unittest.TestCase):


    def test_canProducePlaylistForGivenRecording(self):
        pf = PlaylistFactory()
        recorder_list = MagicMock()
        now = time()
        playlist = pf.produce(recorder_list, start_date_time=now, end_date_time=now+1800)
        self.assertIsInstance(playlist, Playlist)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()