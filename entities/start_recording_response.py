'''
Created on Feb 27, 2013

@author: dough
'''

class StartRecordingResponse(object):
    '''
    classdocs
    '''

    SUCCESS = 0
    SOURCE_NOT_FOUND = 1
    
    def __init__(self, result):
        '''
        Constructor
        '''
        self._result = result
    
    @property
    def result(self):
        return self._result