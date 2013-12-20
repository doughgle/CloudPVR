'''
Created on Jan 9, 2013

@author: dough
'''

import web
from web import form
import time    
        
class ScheduleRecordingPresenter(object):
    
    date_time_picker_link = '''<a href="javascript:NewCal('%s','ddmmmyyyy',true,24)">
        <img src="static/images/cal.gif" width="16" height="16" border="0" alt="Pick a date">
    </a>'''
    
    fields = form.Form(
                            form.Textbox("name", description="Recording Schedule Name"),    
                            form.Dropdown("source", args=[], description="Channel"),
                            form.Textbox("start", post=(date_time_picker_link % "start"), description="Start"),
                            form.Textbox("end", post=(date_time_picker_link % "end"), description="End"),
                            )
    
    controls = form.Form(
                         form.Button("schedule", type="submit", description="Schedule"),
                         form.Button("cancel", type="submit", description="Don't schedule")
                         )
                               
    def __init__(self):
        self.render = web.template.render('templates', base='layout') # your templates
         
    def present(self, source_list):
        fields_form = self.fields()
        fields_form.source.args = source_list
        controls_form = self.controls()
        return self.render.schedule_recording_view(fields_form, controls_form)
    
    def convert_datetime_pres_to_req_format(self, date_time_str):
        try:            
            tm_struct = time.strptime(date_time_str, '%d-%b-%Y %H:%M:%S')
            result = int(time.mktime(tm_struct))
        except ValueError:
            result = None
        return result