'''
Created on Feb 21, 2013

@author: dough
'''
from cancel_recording_schedule_response import CancelRecordingScheduleResponse

class CancelRecordingScheduleController(object):
    '''
    classdocs
    '''


    def __init__(self, master_recording_schedule_list):
        '''
        Constructor
        '''
        self._master_recording_schedule_list = master_recording_schedule_list        
        self._resp = CancelRecordingScheduleResponse(CancelRecordingScheduleResponse.SCHEDULE_DOES_NOT_EXIST)
            
    def cancel(self, request):
        for rec_sch in self._master_recording_schedule_list:
            if rec_sch.id == request.schedule_id:
                self._master_recording_schedule_list.remove(rec_sch)
                rec_sch.cancel()
                self._resp = CancelRecordingScheduleResponse(CancelRecordingScheduleResponse.SUCCESS)
        return self._resp