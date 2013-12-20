'''
Created on Jan 9, 2013

@author: dough
'''
from recording_schedule_request import RecordingScheduleRequest
from view_sources_request import ViewSourcesRequest
from schedule_recording_presenter import ScheduleRecordingPresenter       
import web

class ScheduleRecordingWebController(object):
    '''
    classdocs
    '''        
    
    _application_boundary = None
    _schedule_recording_use_case_controller = None
    _presenter = ScheduleRecordingPresenter()
    
    @staticmethod
    def set_application_boundary(application_boundary):
        ScheduleRecordingWebController._application_boundary = application_boundary

    def GET(self):        
        req = ViewSourcesRequest()
        self.resp = self._application_boundary.list_sources(req)    
        self._source_list = []
        for source in self.resp.sources:
            self._source_list.append((source.id, source.name))      
        return self._presenter.present(self._source_list)        
    
    def POST(self):        
        input_data = web.input()
        if hasattr(input_data, 'schedule'):
            req = self._build_recording_schedule_request(input_data)
            # pass through boundary to use case controller
            resp = self._application_boundary.schedule(req)
            result = resp
            raise web.seeother('/schedules')
        else:
            result = "Go back"
        return result             

    def _build_recording_schedule_request(self, input_data):
        user = 0
        name = input_data.name
        source = int(input_data.source)
        start_date_time = self._presenter.convert_datetime_pres_to_req_format(input_data.start)
        end_date_time = self._presenter.convert_datetime_pres_to_req_format(input_data.end)
        req = RecordingScheduleRequest(user, name, source, start_date_time, end_date_time)
        return req