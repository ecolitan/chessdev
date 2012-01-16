class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class PositionError(Error):
    """Exception raised for errors in position legality."""
    
    def __init__(self, position, message):
        self.position = position
        self.message = message
    def __str__(self):
        return repr(self.position, self.message)

class RelationError(Error):
    """Exception raised for errors in position relationships."""
    
    def __init__(self, p1, p2, message):
        self.p1 = p1
        self.p2 = p2
        self.message = message
    def __str__(self):
        return repr(self.p1, self.p2, self.message)

class DeadlyError(Error):
    """Exception raised for deadly errors."""
    
    def __init__(self, error, message):
        self.error = error
        self.message = message
        
    def __str__(self):
        return repr(self.error, self.message)
