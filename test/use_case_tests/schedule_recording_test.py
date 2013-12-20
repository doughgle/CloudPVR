'''
Created on Dec 27, 2012

@author: dough
'''
import unittest
from recording_schedule_request import RecordingScheduleRequest
from recording_schedule_response import RecordingScheduleResponse
from source_factory import SourceFactory
from schedule_recording_controller import ScheduleRecordingController

        
class TestScheduleRecording(unittest.TestCase):


    def setUp(self):
        sf = SourceFactory()
        master_source_list = []
        one_channel_conf_str = "Digital 8:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:34:98:2"
        master_source_list.append(sf.produce(one_channel_conf_str))        
        self._user_id = 0
        self._schedule_name = "my schedule"
        self._source_id = master_source_list[0].id
        self.master_recording_schedule_list = []
        self.controller = ScheduleRecordingController(master_source_list, self.master_recording_schedule_list)
                
    def test_scheduleImmediateRecording(self):
        req = RecordingScheduleRequest(self._user_id, self._schedule_name, self._source_id)
        resp = self.controller.schedule(req)
        self.assertIsInstance(resp, RecordingScheduleResponse)
        self.assertEqual(resp.result, RecordingScheduleResponse.SUCCESS)
        self.assertIsNotNone(resp.recording_schedule)
        
    def test_schedulingWithNonExistantSourceIsSourceDoesNotExistError(self):        
        self._source_id = 0xFFFFAAAA
        req = RecordingScheduleRequest(self._user_id, self._schedule_name, self._source_id)
        resp = self.controller.schedule(req)
        self.assertIsInstance(resp, RecordingScheduleResponse)
        self.assertEqual(resp.result, RecordingScheduleResponse.SOURCE_DOES_NOT_EXIST)
        self.assertIsNone(resp.recording_schedule)
        
    def test_afterSuccessfulRecordingRequest_recordingScheduleListIsNotEmpty(self):  
        req = RecordingScheduleRequest(self._user_id, "my_recording", self._source_id)
        resp = self.controller.schedule(req)
        self.assertEqual(resp.result, RecordingScheduleResponse.SUCCESS)        
        self.assertEqual(len(self.master_recording_schedule_list), 1)        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()