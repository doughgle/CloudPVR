'''
Created on Dec 27, 2012

@author: dough
'''
from dvbt_source import DVBTSource


class SourceFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._channels_conf_factory = ChannelsConfSourceFactory()
    
    def produce(self, str):
        return self._channels_conf_factory.produce(str)
    
    def produce_batch(self, file_obj):        
        return self._channels_conf_factory.produce_batch(file_obj)
    

class ChannelsConfSourceFactory(object):
    
    def produce(self, str):
        source_attributes = str.split(':')
        return DVBTSource(source_attributes[0], source_attributes[1], source_attributes[-1:][0])
    
    def produce_batch(self, file_obj):
        self._channels_conf = file_obj
        self._channel_list = self._channels_conf.readlines()
        self._channels_conf.close()
        self._source_list = []
        for channel in self._channel_list:
            self._source_list.append( self.produce(channel) )
        return self._source_list    