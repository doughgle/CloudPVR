'''
Created on May 29, 2013

@author: dough
'''
from playback_recording_response import PlaybackRecordingResponse
from playlist_factory import PlaylistFactory

class PlaybackRecordingController(object):
    '''
    classdocs
    '''


    def __init__(self, recordings_list):
        '''
        Constructor
        '''
        self._recordings_list = recordings_list
        self._pf = PlaylistFactory()
    
    def playback(self, req):
        resp = PlaybackRecordingResponse(PlaybackRecordingResponse.RECORDING_DOES_NOT_EXIST)
        for recording in self._recordings_list:
            if recording.id == req.recording_id:
                playlist = self._pf.produce(recording.source, recording.start_date_time, recording.end_date_time)
                resp = PlaybackRecordingResponse(PlaybackRecordingResponse.SUCCESS, playback_url=playlist.url)
                break
            
        return resp