'''
Created on Jan 10, 2013

@author: dough
'''
import unittest
from view_schedules_request import ViewSchedulesRequest
from view_schedules_controller import ViewSchedulesController
from view_schedules_response import ViewSchedulesResponse
from recording_schedule import RecordingSchedule
from source import Source

class TestViewRecordingSchedules(unittest.TestCase):

    def setUp(self):
        self._setup_controller()
        self.req = ViewSchedulesRequest()
        self.resp = self.controller.list_schedules(self.req)
        self._setup_sample_recording_schedule()

    def _setup_controller(self):
        self.master_schedule_list = []
        self.controller = ViewSchedulesController(self.master_schedule_list)

    def _setup_sample_recording_schedule(self):
        self.source = Source('dummy source')
        self.rec_sch = RecordingSchedule(self.source)
        
    def test_viewMasterScheduleList(self):
        self.assertIsInstance(self.resp, ViewSchedulesResponse)
    
    def test_viewEmptyScheduleList(self):
        self.assertEqual(self.resp.result, ViewSchedulesResponse.SUCCESS)
        self.assertEqual(self.resp.length, 0)
                
    def test_lengthAttributeEqualsTheNumberOfRecordingSchedules(self):
        num_schedules = 10
        for schedule in range(num_schedules):
            self.master_schedule_list.append(schedule)            
        self.resp = self.controller.list_schedules(self.req)
        self.assertEqual(self.resp.result, ViewSchedulesResponse.SUCCESS)
        self.assertEqual(self.resp.length, num_schedules)
        
    def test_verifyRecordingScheduleName(self):
        self.master_schedule_list.append(self.rec_sch)
        self.resp = self.controller.list_schedules(self.req)
        self.assertEqual(self.resp.schedules[0].name, "")
        
    def test_verifyRecordingScheduleSource(self):        
        self.master_schedule_list.append(self.rec_sch)
        self.resp = self.controller.list_schedules(self.req)
        self.assertEqual(self.resp.schedules[0].source, self.source)
        self.assertEqual(self.resp.schedules[0].source.name, "dummy source")
        
    def test_verifyRecordingScheduleHasIntegerStartTime(self):
        self.master_schedule_list.append(self.rec_sch)
        self.resp = self.controller.list_schedules(self.req)
        self.assertIsInstance(self.resp.schedules[0].start_date_time, int)        
    
    def test_verifyRecordingScheduleHasIntegerEndTime(self):
        self.master_schedule_list.append(self.rec_sch)
        self.resp = self.controller.list_schedules(self.req)
        self.assertIsInstance(self.resp.schedules[0].end_date_time, int)
 
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()