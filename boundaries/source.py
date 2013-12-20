'''
Created on Dec 28, 2012

@author: dough
'''
class IncompatibleRecorderError(Exception): pass

class Source(object):
    '''
    classdocs
    '''
    __id = 0

    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
        self._recorders = []
        self._id = Source.__id
        Source.__id += 1        
        
    def __str__(self):
        return '%s %d:"%s"' %(Source.__name__, self._id, self._name)

    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id

    @property
    def recorders(self):
        return self._recorders
            
    def start_recording(self):
        for recorder in self._recorders:
            recorder.start()

    def stop_recording(self):
        for recorder in self._recorders:
            recorder.stop()

    def add_recorder(self, recorder):
        self._recorders.append(recorder)