'''
Created on Jan 10, 2013

@author: dough
'''
from view_schedules_response import ViewSchedulesResponse

class ViewSchedulesController(object):
    '''
    classdocs
    '''


    def __init__(self, master_schedule_list):
        '''
        Constructor
        '''
        self._master_schedule_list = master_schedule_list
    
    def list_schedules(self, request):
        return ViewSchedulesResponse(result=ViewSchedulesResponse.SUCCESS, 
                                     schedules=self._master_schedule_list)