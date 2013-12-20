'''
Created on Jan 7, 2013

@author: dough
'''
from view_sources_response import ViewSourcesResponse

class ViewSourcesController(object):
    '''
    classdocs
    '''


    def __init__(self, master_source_list):
        '''
        Constructor
        '''
        self._master_source_list = master_source_list
    
    def list_sources(self, request):
        return ViewSourcesResponse(self._master_source_list)