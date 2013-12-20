'''
Created on May 29, 2013

@author: dough
'''
import unittest
from m3u8_playlist import M3U8Playlist, PlaylistAlreadyTerminated, SegmentDurationExceedsTargetDurationError
from StringIO import StringIO

class TestM3U8Playlist(unittest.TestCase):

    
    def setUp(self):
        self.pl = M3U8Playlist()
    
    def test_playlistFirstLineMustBeExtendedM3UTag(self):
        pl_file = StringIO(str(self.pl))
        self.assertEqual(pl_file.readline().strip(), self.pl.HEADER_TAG)
        
    def test_targetDurationTagAppearsOnceInPlaylist(self):
        pl_str = str(self.pl)
        self.assertEqual(pl_str.count(self.pl.TARGET_DURATION_TAG), 1)

    def test_targetDurationIsInWholeSeconds(self):
        self.assertIsInstance(self.pl.target_duration, int)
        
    def test_targetDurationIsGreaterThanZeroSeconds(self):
        self.assertGreater(self.pl.target_duration, 0)
        
    def test_targetDurationCanBeChangedAfterConstruction(self):
        self.pl.target_duration = 4
        self.assertIn(self.pl.TARGET_DURATION_TAG + '4', str(self.pl))        
    
    def test_endTerminatesPlaylistWithEndListTag(self):
        self.pl.end()
        pl_file = StringIO(self.pl)
        lines = pl_file.readlines()
        last_line = lines[-1:][0]
        self.assertEqual(last_line, self.pl.ENDLIST_TAG)
        
    def test_callingEndTwiceIsPlaylistAlreadyTerminated(self):
        self.pl.end()
        self.assertRaises(PlaylistAlreadyTerminated, self.pl.end)
        
    def test_addSegmentInsertsMediaSegmentTagWithDuration(self):
        self.pl.add_segment(1, 'relative_path', 'artist - vid')
        pl_str = str(self.pl)
        self.assertIn(self.pl.MEDIA_SEGMENT_TAG, pl_str)
        lines = pl_str.splitlines()
        for line in lines:
            if self.pl.MEDIA_SEGMENT_TAG in line:
                inf = line.strip(self.pl.MEDIA_SEGMENT_TAG)
                duration = inf.split(',')[0]
                self.assertEqual(str(duration), str(1))
                
    def test_addSegmentInsertsPathToMediaSegmentOnTheLineFollowingMediaSegmentTag(self):
        given_seg_path = 'relative_path'
        self.pl.add_segment(1, given_seg_path, 'artist - vid')
        pl_str = str(self.pl)
        lines = pl_str.splitlines()
        for i in range(0, len(lines)):
            if self.pl.MEDIA_SEGMENT_TAG in lines[i]:
                segment_path = lines[i+1]     
                self.assertEqual(segment_path, given_seg_path)                
            
    def test_addingSegmentAfterPlaylistTerminated_isPlaylistAlreadyTerminated(self):
        self.pl.end()
        self.assertRaises(PlaylistAlreadyTerminated, self.pl.add_segment, 1, '')
        
    def test_segmentDurationGreaterThanTargetDuration_isTargetDurationExceededError(self):
        self.pl = M3U8Playlist(5)
        self.assertRaises(SegmentDurationExceedsTargetDurationError, self.pl.add_segment, 5.5, 'path')
    
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()