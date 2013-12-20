'''
Created on Feb 25, 2013

@author: dough
'''

class ViewRecordingsResponse(object):
    '''
    classdocs
    '''
    SUCCESS = 0

    def __init__(self, recordings_list):
        '''
        Constructor
        '''
        self._result = self.SUCCESS
        self._recordings = recordings_list
    
    @property
    def result(self):
        return self._result
    
    @property
    def recordings(self):
        return self._recordings