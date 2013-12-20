'''
Created on Dec 27, 2012

@author: dough
'''

class RecordingScheduleResponse(object):
    
    (
     SUCCESS,
     INVALID_CHANNEL,
     SOURCE_DOES_NOT_EXIST
     ) = range(3)
    
    def __init__(self, result):
        self._result = result
        self._recording_schedule = None
    
    def __str__(self):
        return '%s:%d %s' %(RecordingScheduleResponse.__name__, self._result, self._recording_schedule)
    
    @property
    def result(self):
        return self._result
    
    @property
    def recording_schedule(self):
        return self._recording_schedule
    
    @recording_schedule.setter
    def recording_schedule(self, recording_schedule):
        self._recording_schedule = recording_schedule