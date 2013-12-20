'''
Created on May 29, 2013

@author: dough
'''
import unittest
from playback_recording_request import PlaybackRecordingRequest
from playback_recording import PlaybackRecordingController
from playback_recording_response import PlaybackRecordingResponse
import urllib2
from mock import MagicMock

class TestPlaybackRecording(unittest.TestCase):

    
    def setUp(self):
        self.recordings_list = []
        self.mock_recording = MagicMock()
        self.mock_recording.id = 0x0000
                
    def test_playbackACompletedRecording(self):        
        self.recordings_list.append(self.mock_recording)
        req = PlaybackRecordingRequest(recording_id=0x0000)
        self.controller = PlaybackRecordingController(self.recordings_list)
        resp = self.controller.playback(req)
        self.assertIsInstance(resp, PlaybackRecordingResponse)
        self.assertEqual(resp.result, PlaybackRecordingResponse.SUCCESS)
        
    def test_playbackANonExistingRecording_isARecordingDoesNotExistError(self):
        req = PlaybackRecordingRequest(recording_id=0x0000)
        self.controller = PlaybackRecordingController(self.recordings_list)
        resp = self.controller.playback(req)
        self.assertEqual(resp.result, PlaybackRecordingResponse.RECORDING_DOES_NOT_EXIST)
        
    def test_aSuccessfulPlaybackRecordingRequestIsAnsweredWithAPlaylistUrl(self):        
        self.recordings_list.append(self.mock_recording)
        req = PlaybackRecordingRequest(recording_id=0x0000)
        self.controller = PlaybackRecordingController(self.recordings_list)
        resp = self.controller.playback(req)
        self.assertEqual(resp.result, PlaybackRecordingResponse.SUCCESS)
        self.assertIsInstance(resp.playback_url, str)
        self.assertEqual(urllib2.urlopen(resp.playback_url).code, 200)
        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()