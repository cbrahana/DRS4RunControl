import socket

class RunStarter:
    def __init__(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((HOST,PORT))
    def startRun(runName,num_events):
        runstring = "startRun " + runName + " " + n
    
    
