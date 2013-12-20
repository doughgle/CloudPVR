'''
Created on May 30, 2013

@author: dough
'''
from os import linesep

class PlaylistAlreadyTerminated(Exception): pass
class SegmentDurationExceedsTargetDurationError(Exception): pass

class M3U8Playlist(object):
    
    HEADER_TAG =            '#EXTM3U'
    TARGET_DURATION_TAG =   '#EXT-X-TARGETDURATION:'
    MEDIA_SEGMENT_TAG =     '#EXTINF:'
    ENDLIST_TAG =           '#EXT-X-ENDLIST'
    
    def __init__(self, target_duration=10):
        self._terminated = False
        self._target_duration = target_duration
        self._target_duration_tag = self.TARGET_DURATION_TAG + str(self.target_duration)
        self.lines = [self.HEADER_TAG, self._target_duration_tag]
    
    @property
    def target_duration(self):
        return self._target_duration
    
    @target_duration.setter
    def target_duration(self, new_duration):
        new_target_duration_tag = self.TARGET_DURATION_TAG + str(new_duration)
        self.lines = [line.replace(self._target_duration_tag, new_target_duration_tag) for line in self.lines]
    
    def __str__(self):
        if self._terminated:
            self.lines.append(self.ENDLIST_TAG)
        return linesep.join(self.lines)
        
    def add_segment(self, duration_in_secs, path, title=''):
        if not self._terminated:            
            if duration_in_secs > self.target_duration:
                raise SegmentDurationExceedsTargetDurationError()
            segment_tag = self.MEDIA_SEGMENT_TAG + str(duration_in_secs) + ',' + title 
            self.lines.append(segment_tag)
            self.lines.append(path)
        else:
            raise PlaylistAlreadyTerminated()
    
    def end(self):
        if not self._terminated:            
            self._terminated = True
        else:
            raise PlaylistAlreadyTerminated()
        
        
if __name__ == '__main__':
    pl = M3U8Playlist()
    pl.add_segment(10, 'path')
    pl.add_segment(10, 'path')
    pl.end()
    print pl