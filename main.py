#!/usr/bin/env python

import sys
import profile
import time
from test import *

def main():
    """Documentation string here."""
    
    #some testing
    quicktest()


if __name__ == '__main__':
    start_time = time.time()
    #profile.run('main()')
    main()
    print time.time() - start_time, "seconds"
