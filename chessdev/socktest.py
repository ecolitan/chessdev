import sys
import socket
import threading
import time
import Queue

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
            text = raw_input('type here: ') 
            input_queue.put(text)
        return True

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

def main():
    collect_incoming_data = CollectInput()
    collect_incoming_data.start()
    while True:
        if not input_queue.empty():
            text = input_queue.get()
            if text == 'quit':
                collect_incoming_data.stop()
                break
            print "You wrote: ", text, "\n"
            input_queue.task_done()
        time.sleep(0.1) 
    collect_incoming_data.join()
    
if __name__ == '__main__':
    main()
    
