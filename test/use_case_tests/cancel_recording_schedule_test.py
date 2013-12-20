'''
Created on Feb 21, 2013

@author: dough
'''
import unittest
from cancel_recording_schedule_controller import CancelRecordingScheduleController
from cancel_recording_schedule_request import CancelRecordingScheduleRequest
from cancel_recording_schedule_response import CancelRecordingScheduleResponse
from recording_schedule import RecordingSchedule


class TestCancelRecordingSchedule(unittest.TestCase):

    def setUp(self):
        self.master_recording_schedule_list = []
        self.rec_sch = RecordingSchedule(0)
        self.rec_sch.schedule()
        self.master_recording_schedule_list.append(self.rec_sch)
        self.controller = CancelRecordingScheduleController(self.master_recording_schedule_list)
        self._schedule_id = 0x0
        self.req = CancelRecordingScheduleRequest(self._schedule_id)
    
    def test_cancellingANonExistantRecordingScheduleIsDoesNotExistError(self):
        self._schedule_id = 0xFFFFAAAA
        self.req = CancelRecordingScheduleRequest(self._schedule_id)
        resp = self.controller.cancel(self.req)
        self.assertIsInstance(resp, CancelRecordingScheduleResponse)
        self.assertEqual(resp.result, CancelRecordingScheduleResponse.SCHEDULE_DOES_NOT_EXIST)
        
    def test_afterCancellationTheRecordingScheduleIsNotLongerInTheRecordingScheduleList(self):          
        resp = self.controller.cancel(self.req)
        self.assertEqual(resp.result, CancelRecordingScheduleResponse.SUCCESS)
        self.assertEqual(len(self.master_recording_schedule_list), 0)

    def test_afterCancellation_RecordingScheduleStatusIsCancelled(self):
        resp = self.controller.cancel(self.req)
        self.assertEqual(resp.result, CancelRecordingScheduleResponse.SUCCESS)
        self.assertEqual(self.rec_sch.status, RecordingSchedule.STATUS_CANCELLED)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()