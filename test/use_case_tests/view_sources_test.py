'''
Created on Jan 7, 2013

@author: dough
'''
import unittest
from view_sources_request import ViewSourcesRequest
from view_sources_response import ViewSourcesResponse
from view_sources_controller import ViewSourcesController
from source_factory import SourceFactory


class TestViewSources(unittest.TestCase):

    def setUp(self):
        sf = SourceFactory()
        master_source_list = []
        master_source_list.append(sf.produce('Digital 8:538000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_2_3:FEC_1_2:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_16:HIERARCHY_NONE:34:98:2'))
        self.controller = ViewSourcesController(master_source_list)        
        req = ViewSourcesRequest()
        self.resp = self.controller.list_sources(req)
        self.assertEqual(self.resp.result, ViewSourcesResponse.SUCCESS)
            
    def test_viewMasterSourceList(self):        
        self.assertIsInstance(self.resp, ViewSourcesResponse)
        self.assertIsInstance(self.resp.length, int)
        
    def test_masterSourceListShouldHaveOneSource(self):
        self.assertEqual(self.resp.result, ViewSourcesResponse.SUCCESS)
        self.assertEqual(self.resp.length, 1)
        
    def test_verifySourceName(self):
        self.assertEqual(self.resp.result, ViewSourcesResponse.SUCCESS)        
        self.assertEqual(self.resp.sources[0].name, "Digital 8")
        
    def test_verifySourceType(self):
        for source in self.resp.sources:
            self.assertEqual(source.type_str, "DVBTSource")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()