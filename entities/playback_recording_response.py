'''
Created on May 29, 2013

@author: dough
'''

class PlaybackRecordingResponse(object):
    '''
    classdocs
    '''
    
    SUCCESS = 0
    RECORDING_DOES_NOT_EXIST = 1

    def __init__(self, result, playback_url=''):
        '''
        Constructor
        '''
        self._result = result
        self._playlist_url = playback_url
    
    @property
    def result(self):
        return self._result
    
    @property
    def playback_url(self):
        return self._playlist_url