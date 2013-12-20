'''
Created on Dec 28, 2012

@author: dough
'''
import unittest
from mock import MagicMock, create_autospec
from source import IncompatibleRecorderError
from dvbt_source import DVBTSource as Source
from recorder import VideoRecorder

class TestSource(unittest.TestCase):

    def setUp(self):
        self.source = Source("dummy source")
        self.recorder = MagicMock()

    def test_afterCreationSourceHasNoRecorders(self):
        self.assertEqual(len(self.source.recorders), 0)
        
    def test_canAssignMultipleRecordersToSource(self):        
        num_recorders = 3
        for i in range(num_recorders):
            self.source.add_recorder(self.recorder)
        self.assertEqual(len(self.source.recorders), num_recorders)
        
    def test_sourceConfiguresTheRecorderItselfWithSourceTypeSpecificConfig(self):
        self.recorder.configure = MagicMock()
        self.source.add_recorder(self.recorder)
        self.assertTrue(self.recorder.configure.called)
    
    def test_recorderMustBeCompatibleElseIncompatibleRecorderError(self):
        self.recorder.configure = create_autospec(VideoRecorder().configure)
        self.assertRaises(IncompatibleRecorderError, self.source.add_recorder, self.recorder )
            
    def test_whenRecordIsStartedOnSource_AllItsRecordersStart(self):
        self.source.add_recorder(self.recorder)
        self.source.start_recording()
        for recorder in self.source.recorders:
            recorder.start.assert_called_once_with()
            self.assertTrue(recorder.is_recording())
            
    def test_whenSourceIsToldToStopRecording_allItsRecordersStop(self):
        self.recorder.is_recording.return_value = False
        self.source.add_recorder(self.recorder)
        self.source.start_recording()
        self.source.stop_recording()  
        for recorder in self.source.recorders:
            recorder.stop.assert_called_once_with()
            self.assertFalse(recorder.is_recording())
            
    def test_eachNewSourceIsGivenANewId(self):
        source_id_list = []
        num_sources = 3
        for i in range(num_sources):
            source = Source("My source")
            source_id_list.append(source.id)
        self.assertEqual(len(source_id_list), len(set(source_id_list)))
            
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()