'''
Created on Feb 25, 2013

@author: dough
'''
from view_recordings_response import ViewRecordingsResponse

class ViewRecordingsController(object):
    '''
    classdocs
    '''


    def __init__(self, master_recordings_list):
        '''
        Constructor
        '''
        self._master_recordings_list = master_recordings_list
    
    def list_recordings(self, req):        
        return ViewRecordingsResponse(self._master_recordings_list)