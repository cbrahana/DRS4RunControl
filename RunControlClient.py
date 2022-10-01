import socket

class RunStarter:
    def __init__(self, HOST=128.111.19.39, PORT=52090):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.s:
            self.s.connect((HOST,PORT))
    def startRun(runName,num_events):
        runstring = "startRun " + runName + " " + n
        self.s.
    
