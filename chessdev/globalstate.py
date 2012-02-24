import sys
from chessdev.data.data import *

class GlobalState(object):
    """Object to hold global state information."""
    
    def __init__(self):
        self.memory = None
        self.cores = None
        self.nps = None
        self.egtpath = None
        self.ponder = None
        self.timecontrol = None
        self.colour = None
        self.machinename = None
        self.version = None
        self.random = None
        self.supported_variants = None
        self.game_variant = None
        self.valid_cecp_prot = None
        self.post_thinking = None
        self.analyze_mode = None
        self.opponent_name = None
        self.opponent_rating = None
        self.machine_rating = None
        self.ics_game = None
        self.opponent_is_machine = None
        self.cache = None
        self.always_display = None
        self.max_threads = None
        
    def read_config_file(self):
        """Update state from config_file"""
        pass
