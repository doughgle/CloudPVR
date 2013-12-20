'''
Created on Dec 21, 2012

@author: dough
'''
from time import time

class StartTimeHasPassedError(Exception): pass
class EndTimeHasPassedError(Exception): pass
class EndBeforeStartError(Exception): pass
class NotScheduledError(Exception): pass
class NotStartedError(Exception): pass

class RecordingSchedule(object):
    '''
    classdocs
    '''

    DEFAULT_DURATION = 1800
    
    (
    STATUS_NOT_SCHEDULED,
    STATUS_SCHEDULED,
    STATUS_ACTIVE,
    STATUS_CANCELLED,
    STATUS_COMPLETE,
    STATUS_STOPPED,
    ) = range(6)

    def __init__(self, source, start_date_time=None, end_date_time=None, name='' ):
        '''
        Constructor
        '''
        self._id = 0
        self._name = name
        self._creation_time = int(time())
        self._source = source
        self._status = self.STATUS_NOT_SCHEDULED
        
        if start_date_time is None:
            self._set_default_start()
        else:
            self._start_date_time = start_date_time
        self._validate_start()
            
        if end_date_time is None:
            self._set_default_end()
        else:
            self._end_date_time = end_date_time        
        self._validate_end()

    def _validate_start(self):
        if self._start_date_time < self._creation_time:
            raise StartTimeHasPassedError

    def _validate_end(self):
        if self._end_date_time < self._creation_time:
            raise EndTimeHasPassedError
        if self._end_date_time <= self._start_date_time:
            raise EndBeforeStartError
        
    def _set_default_start(self):
        self._start_date_time = self._creation_time

    def _set_default_end(self):
        self._end_date_time = self._start_date_time + self.DEFAULT_DURATION

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
                
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status
        
    @property
    def source(self):
        return self._source
    
    @property
    def start_date_time(self):
        return self._start_date_time
    
    @property
    def end_date_time(self):
        return self._end_date_time
    
    def schedule(self):
        self._status = self.STATUS_SCHEDULED
    
    def cancel(self):
        if (self._status == self.STATUS_SCHEDULED) or (self._status == self.STATUS_ACTIVE):
            self._status = self.STATUS_CANCELLED
        else:
            raise NotScheduledError
    
    def start_recording(self):            
        self._source.start_recording()
        self._status = self.STATUS_ACTIVE
    
    def stop_recording(self):
        if self._status == self.STATUS_ACTIVE:
            self._source.stop_recording()
            self._status = self.STATUS_COMPLETE
        else:
            raise NotStartedError