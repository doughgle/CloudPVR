'''
Created on Jan 4, 2013

@author: dough
'''
from cvlc_recorder import CVLCDVBTRecorder

class RecorderFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def produce(self, source):
        return CVLCDVBTRecorder()