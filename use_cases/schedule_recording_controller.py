'''
Created on Dec 21, 2012

@author: dough
'''

from recording_schedule_response import RecordingScheduleResponse
from recording_schedule import RecordingSchedule

class ScheduleRecordingController(object):
    '''
    classdocs
    '''    

    def __init__(self, master_source_list, master_recording_schedule_list):
        '''
        Constructor
        '''
        self._master_source_list = master_source_list 
        self._master_recording_schedule_list = master_recording_schedule_list

    def schedule(self, recording_schedule_request):        
        if self._is_target_source_valid(recording_schedule_request):                                  
            rec_sch = self._create_recording_schedule(recording_schedule_request)
            self._add_to_recording_schedule_list(rec_sch)
            self._update_recording_schedule_status(rec_sch)
            resp = RecordingScheduleResponse(RecordingScheduleResponse.SUCCESS)
            resp.recording_schedule = rec_sch
        else:
            resp = RecordingScheduleResponse(RecordingScheduleResponse.SOURCE_DOES_NOT_EXIST)
        return resp            
        
    def _is_target_source_valid(self, recording_schedule_request):        
        result = False
        req_source = recording_schedule_request.source_id
        for source in self._master_source_list:
            if source.id == req_source:
                result = True
                break
                        
        return result
    
    def _create_recording_schedule(self, recording_schedule_request):
        for source in self._master_source_list:
            if source.id == recording_schedule_request.source_id:
                return RecordingSchedule(source, 
                                         start_date_time=recording_schedule_request.start_date_time,
                                         end_date_time=recording_schedule_request.end_date_time,
                                         name=recording_schedule_request.name)
    
    def _add_to_recording_schedule_list(self, rec_sch):
        return self._master_recording_schedule_list.append(rec_sch)

    def _update_recording_schedule_status(self, rec_sch):
        rec_sch.status = RecordingSchedule.STATUS_SCHEDULED