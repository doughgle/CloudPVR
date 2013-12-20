'''
Created on May 30, 2013

@author: dough
'''
from playlist import Playlist

class PlaylistFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def produce(self, recorder_list, start_date_time, end_date_time):
        return Playlist(recorder_list[0], start_date_time, end_date_time)