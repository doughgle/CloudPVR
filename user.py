'''
Created on Dec 21, 2012

@author: dough
'''
from recording_schedule_list import RecordingScheduleList


class User(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._my_recording_schedule_list = RecordingScheduleList()
    
    def get_channel_list(self):
        return ('MediaCorp HD5',)
    
    def get_recording_schedule_list(self):
        return self._my_recording_schedule_list