'''
Created on Jan 11, 2013

@author: dough
'''
import web
from time import ctime

class ViewSchedulesPresenter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.render = web.template.render('templates', base='layout') # your templates 
    
    def present(self, schedule_list):
        view_model = self._create_view_model(schedule_list)
        return self.render.recording_schedules_view(view_model)
    
    def _create_view_model(self, schedule_list):
        view_model = []
        for schedule in schedule_list:
            view_model_schedule = ViewModelSchedule(schedule)
            view_model.append(view_model_schedule) 
        return view_model
    

class ViewModelSchedule(object):
        
    status_strings =  {
                          0:'Not Scheduled', 
                          1:'Scheduled',
                          2:'Active',
                          3:'Complete'
                      }
    
    def __init__(self, schedule):
        self._name = schedule.name
        self._start_date_time = ctime(schedule.start_date_time)
        self._end_date_time = ctime(schedule.end_date_time)
        self._source = schedule.source.name #TODO: law of demeter violation!
        self._status = self.status_strings[schedule.status]
        
    @property
    def name(self):
        return self._name
    
    @property
    def start_date_time(self):
        return self._start_date_time
    
    @property
    def end_date_time(self):
        return self._end_date_time
    
    @property
    def source(self):
        return self._source
    
    @property
    def status(self):
        return self._status
    