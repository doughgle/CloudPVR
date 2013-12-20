'''
Created on Dec 21, 2012

@author: dough
'''

class DuplicateScheduleError(Exception): pass

class RecordingScheduleList(list):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        super( RecordingScheduleList, self).__init__()
    
    def append(self, recording_schedule):
        if self._is_duplicate(recording_schedule):
            raise DuplicateScheduleError
      
        super(RecordingScheduleList, self).append(recording_schedule)   
        self._empty = False

    def _is_duplicate(self, recording_schedule):
        result = False                    
        for rec_sch in self:
            if recording_schedule.__dict__ == rec_sch.__dict__:
                result = True

        return result