'''
Created on Dec 28, 2012

@author: dough
'''
from recording_schedule import RecordingSchedule
import time

class RecordingScheduler(object):
    '''
    classdocs
    '''


    def __init__(self, master_schedule_list):
        '''
        Constructor
        '''
        self._master_schedule_list = master_schedule_list
    
    def run(self):            
        while 1:
            self.review()

    def review(self):
        for schedule in self._master_schedule_list:
            if time.time() >= schedule.start_date_time:
                schedule.start_recording()                
            if time.time() >= schedule.end_date_time:
                schedule.stop_recording()                    