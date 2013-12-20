'''
Created on May 29, 2013

@author: dough
'''

class Playlist(object):
    '''
    Create m3u8 playlist hierarchy on the fly based on convention.
    '''


    def __init__(self, recorder, start_date_time, end_date_time=None):
        '''
        Constructor
        '''
        self._url = 'http://google.com'
    
    def __str__(self):
        return ('''#EXTM3U
                   #EXT-X-TARGETDURATION''')
    
    @property
    def url(self):
        return self._url