'''
Created on Dec 27, 2012

@author: dough
'''      
from source import Source, IncompatibleRecorderError

class DVBTSource(Source):
    
    
    def __init__(self, name, dvb_frequency=None, program=None):
        super( DVBTSource, self).__init__(name)
        self._dvb_frequency = dvb_frequency
        self._program = program
    
    @property
    def type_str(self):
        return DVBTSource.__name__
    
    @property
    def dvb_frequency(self):
        return self._dvb_frequency
    
    @property
    def program(self):
        return self._program
    
    def add_recorder(self, recorder):
        try:
            recorder.configure(self._dvb_frequency, self._program)
        except:
            raise IncompatibleRecorderError

        super( DVBTSource, self).add_recorder(recorder)