'''
Created on Dec 21, 2012

@author: dough
'''

class RecordingScheduleRequest(object):
    '''
    classdocs
    '''


    def __init__(self, user, name, source, start_date_time=None, end_date_time=None):
        '''
        Constructor
        '''
        self._user = user
        self._source = source
        self._name = name
        self._start_date_time = start_date_time
        self._end_date_time = end_date_time

    def __str__(self):
        return '%s:"%s" User:%d Source:%d' %(RecordingScheduleRequest.__name__, self._name, self._user, self._source)
                
    @property
    def user(self):
        return self._user

    @property
    def name(self):
        return self._name
        
    @property
    def source_id(self):
        return self._source
    
    @property
    def start_date_time(self):
        return self._start_date_time
    
    @property
    def end_date_time(self):
        return self._end_date_time