'''
Created on Dec 21, 2012

@author: dough
'''
import unittest
from mock import MagicMock
from recording_schedule import *
from time import time
from source import Source


class TestRecordingSchedule(unittest.TestCase):

    def setUp(self):
        self._source = Source("dummy source")
        self.rec_sch = RecordingSchedule(self._source)

    def test_nameDefaultToBlankString(self):
        self.assertEqual(self.rec_sch.name, '')
        
    def test_canBeAssignedAName(self):
        assigned_name = 'My Schedule'
        self.rec_sch.name = assigned_name
        self.assertEqual(self.rec_sch.name, assigned_name)        
                
    def test_targetsASource(self):
        self.assertIsInstance(self.rec_sch.source, Source)
    
    def test_startTimeDefaultsToImmediate(self):                
        self.assertEqual(self.rec_sch.start_date_time, int(time()) )
        
    def test_endTimeDefaultsToStartPlusDefaultDuration(self):
        self.assertEqual(self.rec_sch.end_date_time, self.rec_sch.start_date_time + self.rec_sch.DEFAULT_DURATION)
                
    def test_startTimeCanNotBeInThePast(self):
        start_time = time() - 5
        self.assertRaises(StartTimeHasPassedError, RecordingSchedule, self._source, start_date_time=start_time)
        
    def test_endTimeCanNotBeInThePast(self):
        end_time = time() - 5
        self.assertRaises(EndTimeHasPassedError, RecordingSchedule, self._source, end_date_time=end_time)
        
    def test_endTimeMustBeAfterStartTime(self):
        now = time()
        start_time = now
        end_time = now
        self.assertRaises(EndBeforeStartError, RecordingSchedule, self._source, start_date_time=start_time, 
                          end_date_time=end_time)
        
    def test_startRecordingCallsStartRecordingOnTargetSource(self):
        self._source.start_recording = MagicMock(name='start_recording')
        self.rec_sch.start_recording()        
        self.assertTrue(self._source.start_recording.called)
                
    def test_stopRecordingCallsStopRecordingOnTargetSource(self):
        self.rec_sch.start_recording()
        self._source.stop_recording = MagicMock(name='start_recording')
        self.rec_sch.stop_recording()        
        self.assertTrue(self._source.stop_recording.called)
        
    


class TestRecordingScheduleLifecycleBehaviour(unittest.TestCase):
    
    def setUp(self):
        self._source = Source("dummy source")
        self.rec_sch = RecordingSchedule(self._source)
        
    def test_afterCreation_statusIsNotScheduled(self):
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_NOT_SCHEDULED)

    def test_afterScheduleCalled_statusIsScheduled(self):
        self.rec_sch.schedule()
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_SCHEDULED)    

    def test_afterStartRecording_statusIsActive(self):
        self.rec_sch.start_recording()
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_ACTIVE)

    def test_afterStoppingAnActiveRecording_statusIsComplete(self):
        self.rec_sch.start_recording()
        self.rec_sch.stop_recording()
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_COMPLETE)
        
    def test_cancelledWhenActive_statusIsCancelled(self):
        self.rec_sch.start_recording()
        self.rec_sch.cancel()
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_CANCELLED)
        
    def test_cancelledWhenScheduled_statusIsCancelled(self):
        self.rec_sch.schedule()
        self.rec_sch.cancel()
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_CANCELLED)
        
    def test_cancellingWhenNotScheduledIsNotScheduledError(self):
        self.assertRaises(NotScheduledError, self.rec_sch.cancel)
    
    def test_stopRecordingWhenNotStartedIsNotStartedError(self):
        self.assertRaises(NotStartedError, self.rec_sch.stop_recording)
        


if __name__ == "__main__":
    unittest.main()