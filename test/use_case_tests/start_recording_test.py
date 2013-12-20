'''
Created on Feb 27, 2013

@author: dough
'''
import unittest
from start_recording_request import StartRecordingRequest
from start_recording_controller import StartRecordingController
from start_recording_response import StartRecordingResponse
from recording import Recording
from mock import MagicMock, PropertyMock

class TestStartRecording(unittest.TestCase):

    def setUp(self):
        self.master_source_list = []
        self.mock_source = MagicMock()
        type(self.mock_source).id = PropertyMock(return_value=0)
        self.master_source_list.append(self.mock_source)
        self.master_recordings_list = []
        source_id = 0
        req = StartRecordingRequest("My Recording", source_id)
        controller = StartRecordingController(self.master_source_list, self.master_recordings_list)
        self.resp = controller.start_recording(req)

    def test_whenRecordingIsStarted_systemRespondsWithSuccess(self):        
        self.assertIsInstance(self.resp, StartRecordingResponse)
        self.assertEqual(self.resp.result, StartRecordingResponse.SUCCESS)
        
    def test_whenRecordingIsStartedSuccessfully_newRecordingIsAddedToTheRecordingsList(self):        
        self.assertEqual(self.resp.result, StartRecordingResponse.SUCCESS)
        self.assertEqual(len(self.master_recordings_list), 1)

    def test_whenRecordingIsStartedSuccessfully_recordingStateIsActive(self):
        self.assertEqual(self.resp.result, StartRecordingResponse.SUCCESS)
        self.assertEqual(self.master_recordings_list[0].state, Recording.STATE_ACTIVE) 
            
    def test_masterRecordingsListContainsOnlyRecordings(self):
        for recording in self.master_recordings_list:
            self.assertIsInstance(recording, Recording)
            
    def test_validRequestTriggersStartRecordingCallOnChosenSource(self):
        self.mock_source.start_recording.assert_called_once_with()        


class TestStartRecordingOnInvalidSource(unittest.TestCase):

    def setUp(self):
        self.master_source_list = []
        self.master_recordings_list = []
        source_id = 0xAAAA5555
        req = StartRecordingRequest("My Recording", source_id)
        controller = StartRecordingController(self.master_source_list, self.master_recordings_list)
        self.resp = controller.start_recording(req)
        
    def test_requestingNotExistentSourceIsSourceNotFoundResponse(self):        
        self.assertEqual(self.resp.result, StartRecordingResponse.SOURCE_NOT_FOUND)
        
    def test_recordingIsNotAddedToRecordingsList(self):
        self.assertEqual(len(self.master_recordings_list), 0)
        
        
            

        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()