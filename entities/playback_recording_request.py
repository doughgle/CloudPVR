'''
Created on May 29, 2013

@author: dough
'''

class PlaybackRecordingRequest(object):
    '''
    classdocs
    '''


    def __init__(self, recording_id):
        '''
        Constructor
        '''
        self._recording_id = recording_id
    
    @property
    def recording_id(self):
        return self._recording_id
        