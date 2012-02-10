import sys
import socket
import threading
import time
import Queue
from chessdev.data.data import *

#import pdb; pdb.set_trace()

input_queue = Queue.Queue()

class CollectInput(threading.Thread):
    """Collect input from stdin."""
    def __init__(self):
        super(CollectInput, self).__init__()
        self._stop = threading.Event()
        
    def run(self):
        while True:
            if self.stopped():
                break
            text = raw_input() 
            input_queue.put(text)
        return True

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

class CecpWrapper():
    """Implement the Chess Engine Communication Protocol (CECP)"""
    def __init__(self):
        pass
        
    def GetComands(self):
        """Poll incoming_commands Queue and check if the command is known.
        If unknown, write appropriate response to stdout
        Returns List or None"""
        
        text = input_queue.get(True)
        try:
            words = text.split()        
            if valid_move_input_obj.search(words[0]):
                return words
            elif words[0] in valid_commands:
                return words
            else:
                print "Error (unknown command): ", text
                return None
        except IndexError:
            print "Error (unknown command): ", text
            return None
                

    
