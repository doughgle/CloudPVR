'''
Created on Jan 7, 2013

@author: dough
'''
import web
from view_sources_webcontroller import ViewSourcesWebController
from schedule_recording_webcontroller import ScheduleRecordingWebController
from view_schedules_webcontroller import ViewSchedulesWebController
from application_boundary import ApplicationBoundary

render = web.template.render('templates', base='layout')

urls = (
        '/',        'home',
        '/sources', 'ViewSourcesWebController',
        '/schedule','ScheduleRecordingWebController',
        '/schedules', 'ViewSchedulesWebController',
        '/play',    'Play'    
)

class home(object):
    
    def GET(self):
        name = 'Cloud PVR'    
        return render.index(name)
    
class Play(object):
    
    def GET(self):
        return render.playback()
    
'''For development server use this code'''    
if __name__ == '__main__':
        
    #tie the webcontroller to the application
    application_boundary = ApplicationBoundary()
    ViewSourcesWebController.set_application_boundary(application_boundary)
    ScheduleRecordingWebController.set_application_boundary(application_boundary)
    ViewSchedulesWebController.set_application_boundary(application_boundary)
        
    app = web.application(urls, globals())
    app.run()

'''For deployment use this code'''
#application = web.application(urls, globals(), autoreload=False).wsgifunc()