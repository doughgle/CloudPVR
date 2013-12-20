'''
Created on Dec 28, 2012

@author: dough
'''
import os

class NotConfiguredError(Exception): pass

class VideoRecorder(object):
    '''
    classdocs
    '''
    DEFAULT_DESTINATION = os.path.join(os.getcwd(), "default.vid")

    def __init__(self, video_destination=None):
        '''
        Constructor
        '''
        if video_destination is None:
            self._video_destination = self.DEFAULT_DESTINATION
        else:
            self._video_destination = video_destination
    
    def configure(self):
        pass
    
    def is_recording(self):
        pass
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def reset(self):
        pass