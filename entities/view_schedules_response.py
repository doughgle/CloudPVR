'''
Created on Jan 10, 2013

@author: dough
'''

class ViewSchedulesResponse(object):
    '''
    classdocs
    '''
    SUCCESS = 0

    def __init__(self, result, schedules):
        '''
        Constructor
        '''
        self._result = result        
        self._schedules = schedules
    
    @property
    def result(self):
        return self._result
    
    @property
    def length(self):
        return len(self._schedules)
    
    @property
    def schedules(self):
        return self._schedules