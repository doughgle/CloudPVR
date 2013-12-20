'''
Created on Dec 27, 2012

@author: dough
'''
import unittest
from source_factory import SourceFactory
from StringIO import StringIO

class TestSourceFactory(unittest.TestCase):


    def setUp(self):
        self.src_factory = SourceFactory()        
        
    def test_canProduceSourceFromChannelsConfString(self):
        one_channel_conf_str = "Digital 8:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:34:98:2"
        source = self.src_factory.produce(one_channel_conf_str)
        
    def test_sourceHasNameFromChannelsConfString(self):
        channels_conf_strings = [
                                 "Digital 8:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:34:98:2",
                                 "Digital CNA:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:35:99:3",                                 
                                 "Digital 5:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:33:97:4",
                                 "MediaCorp HD5:610000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_8:HIERARCHY_NONE:33:99:8"
                                ]

        for channel_conf in channels_conf_strings:
            source = self.src_factory.produce(channel_conf)
            self.assertEqual(source.name, channel_conf.split(':')[0])
            
    def test_canProduceBatchOfSourcesFromChannelsConfFile(self):
        file_content = ('''Digital 8:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:34:98:2
        Digital CNA:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:35:99:3                  
        Digital 5:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:33:97:4
        MediaCorp HD5:610000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_8:HIERARCHY_NONE:33:99:8''')
        channels_conf_file = StringIO(file_content)
        source_list = self.src_factory.produce_batch(channels_conf_file)
        self.assertEqual(len(source_list), 4)
        for source in source_list:
            self.assertIsNotNone(source)
            self.assertIsNotNone(source.name)
            self.assertIsInstance(source.name, str)
        


if __name__ == "__main__":
    unittest.main()