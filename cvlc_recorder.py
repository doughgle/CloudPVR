'''
Created on Dec 24, 2012

@author: dough
'''
import subprocess
import signal
import os
from recorder import VideoRecorder, NotConfiguredError  
    
class CVLCDVBTRecorder(VideoRecorder):
    '''
    classdocs
    '''


    def __init__(self, video_destination=None):
        '''
        Constructor
        '''
        super(CVLCDVBTRecorder, self).__init__(video_destination)
        self._is_recording = False
        self._is_configured = False
        self.reset()
    
    def __del__(self):
        self.stop()
               
    @property
    def dvb_frequency(self):
        return self._dvb_frequency
    
    @property
    def program(self):
        return self._program
    
    def configure(self, dvb_frequency, program):
        self._dvb_frequency = dvb_frequency
        self._program = program
        self._is_configured = True
    
    def is_recording(self):
        return self._is_recording
    
    def start(self):
        if not self._is_configured:
            raise NotConfiguredError
        if not self.is_recording():
            self._cvlc_command_line = [
             "cvlc",
             "-vvv",
             "-I",
             "dummy",
             "dvb-t://",
             ":dvb-frequency=%s" % self._dvb_frequency,
             ":dvb-bandwidth=8",
             ":program=%s" % self._program,
             ":sout=#transcode{width=320,height=240,fps=25,vcodec=h264,vb=128,venc=x264{aud,profile=baseline,level=30,"
             "keyint=30,ref=1},acodec=mp3,ab=96,channels=2}:std{access=livehttp{seglen=3,delsegs=false,"
             "numsegs=0,index=/var/www/html/streaming/mystream.m3u8,"
             "index-url=http://192.168.15.25/streaming/mystream-########.ts},"
             "mux=ts{use-key-frames},"             
             "dst=%s-########.ts}" %self._video_destination
            ]           
            stderr_log = open("err_cvlc_recorder.log", 'w')
            stdout_log = open("out_cvlc_recorder.log", 'w')
            self._cvlc = subprocess.Popen(self._cvlc_command_line, stdout=stdout_log, stderr=stderr_log)
            self._is_recording = True
        
    def stop(self):     
        if self.is_recording():
            self._cvlc.send_signal(signal.SIGINT)
            self._cvlc.wait()
        self._is_recording = False
    
    def reset(self):
        self.stop()
    
    
if __name__ == '__main__':
    import time
    recorder = CVLCDVBTRecorder()
    recorder.configure(dvb_frequency=610000000, program=8)
    recorder.start()
    print(recorder._cvlc_command_line)
    time.sleep(15)
    recorder.stop()    