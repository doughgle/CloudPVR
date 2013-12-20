'''
Created on Feb 25, 2013

@author: dough
'''
import unittest
from view_recordings_request import ViewRecordingsRequest
from view_recordings_controller import ViewRecordingsController
from view_recordings_response import ViewRecordingsResponse
from _abcoll import Iterable
from recording import Recording

class TestViewRecordingsList(unittest.TestCase):

    def setUp(self):
        master_recordings_list = []
        master_recordings_list.append(MockRecording())
        self.controller = ViewRecordingsController(master_recordings_list)
        self.req = ViewRecordingsRequest()
        self.resp = self.controller.list_recordings(self.req)
        
    def test_emptyRecordingsListHasZeroLength(self):        
        master_recordings_list = []
        self.controller = ViewRecordingsController(master_recordings_list)
        self.resp = self.controller.list_recordings(self.req)
        self.assertEqual(self.resp.result, ViewRecordingsResponse.SUCCESS)
        self.assertEqual(len(self.resp.recordings), 0)
        
    def test_recordingsListShouldBeIterable(self):
        self.assertIsInstance(self.resp.recordings, Iterable)
        
    def test_recordingsListShouldHaveOneRecording(self):
        self.assertEqual(self.resp.result, ViewRecordingsResponse.SUCCESS)
        self.assertEqual(len(self.resp.recordings), 1)
        
    def test_verifyRecordingName(self):
        self.assertEqual(self.resp.recordings[0].name, "Mock Recording")
        
    def test_verifyRecordingURL(self):
        self.assertEqual(self.resp.recordings[0].destination, "http://destination.example.com")

class MockRecording(Recording):
    
    @property
    def name(self):
        return "Mock Recording"
    
    @property
    def destination(self):
        return "http://destination.example.com"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()