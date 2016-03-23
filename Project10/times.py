class Time( object ):
    def __init__( self, hh=0, mm=0, ss=0, zz=0 ):
        """This method initializes a Time object."""
        pass
    
    def __str__( self ):
        """This method  return a str object which is a printable representation
        of a Time object."""
        return "time string"
    
    def __repr__( self ):
        """This method  return a str object which is a printable representation
        of a Time object."""
        return "time string"
    
    def from_utc( self, utc_str ):
        """This method  accepts a str object (the desired UTC time) and changes
        the value of the Time object."""
        pass
    
    def from_seconds( self, sec ):
        """This method accepts an int object (the number of seconds from the
        start of a day) and changes the value of a Time object."""
        pass
        
    def __eq__( self, other ):
        """This method supports the equal comparison between two Time
        objects."""
        return False
    
    def __ne__( self, other ):
        """This method supports the not equal comparison between two Time
        objects."""
        return False
    
    def __lt__( self, other ):
        """This method supports the less than comparison between two Time
        objects."""
        return False
        
    def __le__( self, other ):
        """This method supports the less or equal comparison between two Time
        objects."""
        return False
        
    def __gt__( self, other ):
        """This method supports the greater than comparison between two Time
        objects."""
        return False
    
    def __ge__( self, other ):
        """This method supports the greater or equal comparison between two
        Time objects."""
        return False
        
    def __add__( self, other ):
        """This method supports the addition of a Time object and an int object
        (which represents a number of seconds)."""
        return self
    
    def __sub__( self, other ):
        """This method supports the subtraction of two Time objects, where the
        result is the number of seconds by which the two times differ."""
        return 0