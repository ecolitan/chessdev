#!/usr/bin/env python

import sys
import profile
import time
import Queue
from test import *

def main():
    """main"""
    
    #Incoming commands must be processed my main thread
    incoming_commands = Queue.Queue()
    
    
    #some testing
    quicktest()

num_runs = 100000

if __name__ == '__main__':
    start_time = time.time()
    
    #for i in xrange (0,num_runs):
    #    main()
    
    main()
    
    simple_time = (time.time() - start_time)/num_runs
    #print simple_time, "seconds per run"
    print 1/simple_time, "NPS"
    
    #profile.run('main()')
