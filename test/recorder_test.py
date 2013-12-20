'''
Created on Dec 24, 2012

@author: dough
'''
import unittest
from cvlc_recorder import CVLCDVBTRecorder as VideoRecorder
from recorder import NotConfiguredError
import os

class TestRecorder(unittest.TestCase):

    def setUp(self):
        self.rec = VideoRecorder(video_destination=os.getcwd())
        self.rec.configure(dvb_frequency=610000000, program=8)
        
    def tearDown(self):
        self.rec.reset()
        
    def test_isNotRecordingAfterInitialisation(self):
        self.assertFalse(self.rec.is_recording())
                             
    def test_isRecordingAfterStartCommandReceived(self):
        self.rec.start()
        self.assertTrue(self.rec.is_recording())
        
    def test_isNotRecordingAfterStopCommand(self):
        self.rec.start()
        self.rec.stop()
        self.assertFalse(self.rec.is_recording())
        
    def test_stopWhenNotRecordingDoesNothing(self):
        self.assertFalse(self.rec.is_recording())
        for x in range(10):
            self.rec.stop()     
        self.assertFalse(self.rec.is_recording())
        
    def test_startWhenAlreadyRecordingDoesNothing(self):
        for x in range(10):
            self.rec.start()
        self.assertTrue(self.rec.is_recording())
        
    def test_resetWhenRecordingStopsTheActiveRecording(self):
        self.rec.start()
        self.assertTrue(self.rec.is_recording())
        self.rec.reset()
        self.assertFalse(self.rec.is_recording())

    def test_startingBeforeConfiguringIsANotConfiguredError(self):
        recorder = VideoRecorder()
        self.assertRaises(NotConfiguredError, recorder.start)

class TestDVBTRecorder(unittest.TestCase):
    
    def setUp(self):
        self.rec = VideoRecorder()
        self.test_freq = 1000
        self.test_prog = 4
    
    def test_configureSetsDVBFrequencyAndProgramTogether(self):         
        self.rec.configure(self.test_freq, self.test_prog)
        self.assertEqual(self.rec.dvb_frequency, self.test_freq)
        self.assertEqual(self.rec.program, self.test_prog)
        
    def test_programCannotBeSetDirectly(self):
        self.assertRaises(AttributeError, setattr, self.rec, 'program', self.test_prog)
    
    def test_dvbFrequencyCannotBeSetDirectly(self):
        self.assertRaises(AttributeError, setattr, self.rec, 'dvb_frequency', self.test_freq)
        
import time
import glob

class TestRecorderActuallyRecordsSomething(unittest.TestCase):
    
    def setUp(self):
        self.filename = "video_recorder_output.test"
        self.path = os.path.join(os.getcwd(), self.filename)
        self.glob_pattern = self.path + '*'        
        for matching_file in glob.glob(self.glob_pattern):
            os.remove(matching_file)        
        self.rec = VideoRecorder(video_destination=self.path)
        self.rec.configure(dvb_frequency=610000000, program=8)
            
    def test_afterStartingAndStoppingAFileIsProduced(self):                
        matching_files_list = glob.glob(self.glob_pattern)
        self.assertEqual(len(matching_files_list), 0)
        self.rec.start()
        time.sleep(2 + 6)
        self.rec.stop()
        matching_files_list = glob.glob(self.glob_pattern)
        self.assertGreaterEqual(len(matching_files_list), 1, "No files matching %s were found!" %self.glob_pattern)
        

        

if __name__ == "__main__":
    unittest.main()