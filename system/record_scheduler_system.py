'''
Created on Jan 2, 2013

@author: dough
'''
from recording_scheduler import RecordingScheduler
from recording_schedule_list import RecordingScheduleList
import threading
from source_factory import SourceFactory
from recorder_factory import RecorderFactory
from schedule_recording_controller import ScheduleRecordingController
from schedule_recording_receptionist import ScheduleRecordingReceptionist
from recording_schedule_request import RecordingScheduleRequest
from recording_schedule_response import RecordingScheduleResponse


if __name__ == '__main__':
#    master_schedule_list = RecordingScheduleList()
    master_schedule_list = []
    master_scheduler = RecordingScheduler(master_schedule_list)
    master_scheduler_thread = threading.Thread(target=master_scheduler.run)
    master_scheduler_thread.start()
    print "running master scheduler..."
    
    # init the available sources
    sf = SourceFactory()
    master_source_list = sf.produce_batch('/home/dough/Downloads/channels.conf')
    print master_source_list
    
    # configure recorders for the sources
    rf = RecorderFactory()
    for source in master_source_list:
        recorder = rf.produce(source)
        source.add_recorder(recorder)
    controller = ScheduleRecordingController(master_source_list, master_schedule_list)
            
    # simulate a schedule recording request
    _user_id = 0
    _schedule_name = "my schedule"
    _source_id = master_source_list[1].id
    req = RecordingScheduleRequest(_user_id, _schedule_name, _source_id)
    print req
    _rxr = ScheduleRecordingReceptionist(controller)
    responder = _rxr.receive(req)                
    resp = responder.get_response()
    assert resp.result == RecordingScheduleResponse.SUCCESS    
        
    master_scheduler_thread.join()