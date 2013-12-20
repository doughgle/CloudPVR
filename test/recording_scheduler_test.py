'''
Created on Dec 28, 2012

@author: dough
'''
import unittest
from recording_scheduler import RecordingScheduler
from recording_schedule import RecordingSchedule
from source import Source
import time
from mock import patch, MagicMock

class TestRecordingScheduler(unittest.TestCase):

    def setUp(self):
        self.master_schedule_list = []
        self.source = Source("dummy source")
        self.future_start_time = time.time() + 60
        self.schedule = RecordingSchedule(self.source)
        self.schedule.start_recording = MagicMock(name='start_recording')
        
    def test_schedulerStartsARecordingImmediately(self):        
        self.master_schedule_list.append(self.schedule)
        self.scheduler = RecordingScheduler(self.master_schedule_list)
        self.scheduler.review()
        self.assertTrue(self.schedule.start_recording.called)
        
    def test_aScheduledFutureRecordingIsNotStartedImmediately(self):        
        self.schedule = RecordingSchedule(self.source, start_date_time=self.future_start_time)
        self.master_schedule_list.append(self.schedule)
        self.scheduler = RecordingScheduler(self.master_schedule_list)
        self.schedule.start_recording = MagicMock(name='start_recording')
        self.scheduler.review()
        self.assertFalse(self.schedule.start_recording.called)
        
    def test_recordingIsStartedWhenStartTimeBecomesNow(self):
        self.schedule = RecordingSchedule(self.source, start_date_time=self.future_start_time)
        self.schedule.start_recording = MagicMock(name='start_recording')
        self.master_schedule_list.append(self.schedule)        
        self.scheduler = RecordingScheduler(self.master_schedule_list)
        with patch('time.time') as mock_time:
            mock_time.return_value = self.future_start_time
            self.scheduler.review()            
        self.assertTrue(self.schedule.start_recording.called)
            
    def test_recordingIsStoppedWhenEndTimeIsReached(self):
        future_end_time = time.time() + 100
        self.schedule = RecordingSchedule(self.source, end_date_time=future_end_time)
        self.schedule.stop_recording = MagicMock(name='stop_recording')
        self.master_schedule_list.append(self.schedule)        
        self.scheduler = RecordingScheduler(self.master_schedule_list)
        with patch('time.time') as mock_time:
            mock_time.return_value = future_end_time
            self.scheduler.review()
        self.assertTrue(self.schedule.stop_recording.called)        



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()