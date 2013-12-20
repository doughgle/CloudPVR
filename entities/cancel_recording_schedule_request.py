'''
Created on Feb 21, 2013

@author: dough
'''

class CancelRecordingScheduleRequest(object):
    '''
    classdocs
    '''


    def __init__(self, schedule_id):
        '''
        Constructor
        '''
        self._schedule_id = schedule_id
        
    @property
    def schedule_id(self):
        return self._schedule_id