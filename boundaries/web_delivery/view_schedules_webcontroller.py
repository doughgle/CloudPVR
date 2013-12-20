'''
Created on Jan 10, 2013

@author: dough
'''
from application_boundary import ApplicationBoundary
from view_schedules_request import ViewSchedulesRequest
from view_schedules_presenter import ViewSchedulesPresenter

class ViewSchedulesWebController(object):
    '''
    classdocs
    '''
    _application_boundary = None
    _presenter = ViewSchedulesPresenter()
    
    @staticmethod
    def set_application_boundary(application_boundary):
        ViewSchedulesWebController._application_boundary = application_boundary
            
    def GET(self):        
        req = ViewSchedulesRequest()
        resp = self._application_boundary.list_schedules(req)
        return self._presenter.present(resp.schedules)       

    def POST(self):
        pass
