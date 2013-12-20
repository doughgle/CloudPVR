'''
Created on Jan 4, 2013

@author: dough
'''
import unittest
from recorder_factory import RecorderFactory
from dvbt_source import DVBTSource
from cvlc_recorder import CVLCDVBTRecorder

class TestRecorderFactory(unittest.TestCase):
        
    def test_canProduceCompatibleRecorderForGivenSource(self):
        rf = RecorderFactory()
        source = DVBTSource("dummy source")
        recorder = rf.produce(source)
        self.assertIsInstance(recorder, CVLCDVBTRecorder)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()