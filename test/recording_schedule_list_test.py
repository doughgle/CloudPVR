'''
Created on Dec 21, 2012

@author: dough
'''
import unittest
from recording_schedule_list import RecordingScheduleList
from recording_schedule_list import DuplicateScheduleError
from recording_schedule import RecordingSchedule
from source import Source
import time

class TestRecordingScheduleList(unittest.TestCase):

    def setUp(self):
        self.rec_sch_list = RecordingScheduleList()
        self.source = Source('dummy source')
        self.recording_schedule = RecordingSchedule(self.source)        
        
    def test_recordingScheduleListIsInitiallyEmpty(self):
        self.assertEqual(len(self.rec_sch_list), 0)
        
    def test_lengthOfListEqualsTheNumberOfRecordingSchedulesAdded(self):        
        num_schedules_added = 0
        for i in range(1,10):
            start = (time.time()+i)
            end = start + i
            rec_sch = RecordingSchedule(self.source, start_date_time=start, end_date_time=end)
            self.rec_sch_list.append(rec_sch)
            num_schedules_added += 1
        self.assertEqual(len(self.rec_sch_list), num_schedules_added)            
        
    def test_addingTheSameScheduleTwiceIsADuplicateScheduleError(self):
        self.rec_sch_list.append(self.recording_schedule)
        self.assertRaises(DuplicateScheduleError, self.rec_sch_list.append, self.recording_schedule)
        
    def test_addingANewScheduleWithStartEndMatchingExisitingSchedule_isADuplicateScheduleError(self):        
        start = time.time() + 3600
        end = start + 1800        
        rec_sch = RecordingSchedule(self.source, start_date_time=start, end_date_time=end)
        self.rec_sch_list.append(rec_sch)
        duplicate_rec_sch = RecordingSchedule(self.source, start_date_time=start, end_date_time=end)
        self.assertRaises(DuplicateScheduleError, self.rec_sch_list.append, duplicate_rec_sch)
        
        

if __name__ == "__main__":
    unittest.main()