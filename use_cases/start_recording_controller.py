'''
Created on Feb 27, 2013

@author: dough
'''
from start_recording_response import StartRecordingResponse
from recording import Recording

class SourceNotFoundError(Exception): pass

class StartRecordingController(object):
    '''
    classdocs
    '''


    def __init__(self, master_source_list, master_recordings_list):
        '''
        Constructor
        '''
        self._master_source_list = master_source_list
        self._master_recordings_list = master_recordings_list
    
    def start_recording(self, request):
        try:
            source = self._get_source(request.source_id)
            source.start_recording()
            new_recording = Recording()
            self._master_recordings_list.append(new_recording)
            result = StartRecordingResponse.SUCCESS
        except SourceNotFoundError:
            result = StartRecordingResponse.SOURCE_NOT_FOUND                                

        return StartRecordingResponse(result)
    
    def _get_source(self, source_id):
        for source in self._master_source_list:
            if source.id == source_id:
                return source            
        raise SourceNotFoundError            