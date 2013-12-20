'''
Created on Feb 21, 2013

@author: dough
'''

class CancelRecordingScheduleResponse(object):
    '''
    classdocs
    '''

    (SUCCESS,
     SCHEDULE_DOES_NOT_EXIST) = range(2)

    def __init__(self, result):
        '''
        Constructor
        '''
        self._result = result
    
    @property
    def result(self):
        return self._result