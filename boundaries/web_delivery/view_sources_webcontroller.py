'''
Created on Jan 9, 2013

@author: dough
'''
from view_sources_request import ViewSourcesRequest

class ViewSourcesWebController(object):
    '''
    classdocs
    '''
    _application_boundary = None
    
    @staticmethod
    def set_application_boundary(application_boundary):
        ViewSourcesWebController._application_boundary = application_boundary
    
    def GET(self):
        req = ViewSourcesRequest()
        self.resp = self._application_boundary.list_sources(req)
        return self.resp.sources

    def POST(self):
        pass
