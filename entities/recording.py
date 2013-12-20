'''
Created on Feb 25, 2013

@author: dough
'''
import os
import uuid

class RecordingDestinationError(Exception): pass

class Recording(object):
    '''
    classdocs
    '''
    DEFAULT_DESTINATION_DIR = os.path.dirname(__file__)
    STATE_ACTIVE = 1

    def __init__(self, destination_dir=None):
        '''
        Constructor
        '''
        self._name = ''        
        self._init_destination(destination_dir)
                
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def destination(self):
        return self._destination
    
    @property
    def filename(self):        
        return 'vid_' + str(uuid.uuid4())
    
    @property
    def destination_dir(self):
        return self._dest_dir
    
    @property
    def state(self):
        return self.STATE_ACTIVE

    def _init_destination(self, destination_dir):
        if destination_dir is None:
            destination_dir = self.DEFAULT_DESTINATION_DIR
        if self._is_destination_dir_valid(destination_dir):
            self._dest_dir = destination_dir
            self._destination = os.path.join(destination_dir, self.filename)
        else:
            raise RecordingDestinationError

    def _is_destination_dir_valid(self, destination):
        try:
            path = os.path.join(destination, "rw_validation.txt")
            rw_validation_file = open(path, 'w')
            rw_validation_file.close()
            os.remove(rw_validation_file.name)
            result = True
        except IOError:
            result = False        
        return result



