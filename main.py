#!/usr/bin/env python

import sys
import profile
import time
import Queue
from test import *
from chessdev.cecp import *
from chessdev.globalstate import *

def main():
    """main"""
    #Initialise global_state object
    global_state = GlobalState()
    global_state.ParseConfig()
    
    #Incoming commands must be processed my main thread
    #input_queue = Queue.Queue()
    #global input_queue
    
    #some testing
    #quicktest()
    collect_incoming_data = CollectInput()
    collect_incoming_data.start()
    while True:
        CecpWrapper().GetComands()
    #collect_incoming_data.stop()
    #collect_incoming_data.join()

num_runs = 100000

if __name__ == '__main__':
    start_time = time.time()
    
    #for i in xrange (0,num_runs):
    #    main()
    
    main()
    
    #simple_time = (time.time() - start_time)/num_runs
    #print simple_time, "seconds per run"
    #print 1/simple_time, "NPS"
    
    #profile.run('main()')
