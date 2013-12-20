'''
Created on Jan 7, 2013

@author: dough
'''

class ViewSourcesResponse(object):
    '''
    classdocs
    '''

    SUCCESS = 0
    
    def __init__(self, source_list):
        '''
        Constructor
        '''
        self._source_list = source_list
    
    @property
    def result(self):
        return ViewSourcesResponse.SUCCESS
    
    @property
    def length(self):
        return 1
    
    @property
    def sources(self):
        return self._source_list