'''
Created on Feb 27, 2013

@author: dough
'''

class StartRecordingRequest(object):
    '''
    classdocs
    '''


    def __init__(self, name, source):
        '''
        Constructor
        '''
        self._source = source
    
    @property
    def source_id(self):
        return self._source