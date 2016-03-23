class Time( object ):
    def __init__( self, hh=0, mm=0, ss=0, zz=0 ):
        """This method initializes a Time object."""
        validate = False
        try:
            if 0 <= hh < 24 and 0 <= mm < 60 and 0 <= ss < 60 and -12 <= zz <= 12:
                validate = True
        except:
            validate = False
        if validate:
            self.hh = hh
            self.mm = mm
            self.ss = ss
            self.zz = zz
        else:
            raise ValueError
    
    def __str__( self ):
        """This method  return a str object which is a printable representation
        of a Time object."""
        if self.zz >= 0:
            sign = "+"
        elif self.zz < 0:
            sign = "-"
        output = str( self.hh ).rjust(2, "0") + ":" + str( self.mm ).rjust(2, "0") + ":" + str( self.ss ).rjust(2, "0") + sign + str( abs(self.zz) ).rjust(2, "0")
        return output
    
    def __repr__( self ):
        """This method  return a str object which is a printable representation
        of a Time object."""
        return self.__str__()
    
    def from_str( self, utc_str ):
        """This method  accepts a str object (the desired UTC time) and changes
        the value of the Time object."""
        try:
            self.hh = int( utc_str[0:2] )
            self.mm = int( utc_str[3:5] )
            self.ss = int( utc_str[6:8] )
            self.zz = int( utc_str[8:11] )
        except:
            raise ValueError
    
    def from_seconds( sec ):
        """This method accepts an int object (the number of seconds from the
        start of a day) and changes the value of a Time object."""
        hh = sec // 3600
        sec = sec % 3600
        mm = sec // 60
        sec = sec % 60
        ss = sec
        return Time( hh, mm, ss )
    
    def get_as_local( self ):
        if self.hh == 12 and self.mm == 0 and self.ss == 0:
            output = "Noon"
        elif self.hh == 0 and self.mm == 0 and self.ss == 0:
            output = "Midnight"
        else:
            AM_PM = "AM"
            if 0 <= self.hh < 12:
                AM_PM = "AM"
            elif 12 <= self.hh < 24:
                AM_PM = "PM"
            
            if 0 < self.hh <= 12:
                hh = self.hh
            elif 12 < self.hh <= 23:
                hh = self.hh - 12
            elif self.hh == 0:
                hh = 12
            
            mm = self.mm
            ss = self.ss
            
            output = str( hh ).rjust(2, "0") + ":" + str( mm ).rjust(2, "0") + ":" + str( ss ).rjust(2, "0") + " " + AM_PM
        
        return output
        
    def __eq__( self, other ):
        """This method supports the equal comparison between two Time
        objects."""
        if type( other ) == Time:
            eq = False
            if self.hh == other.hh and self.mm == other.mm and self.ss == other.ss and self.zz == other.zz:
                eq = True
            return eq
        else:
            raise TypeError
    
    def __ne__( self, other ):
        """This method supports the not equal comparison between two Time
        objects."""
        if type( other ) == Time:
            ne = True
            if self.hh == other.hh and self.mm == other.mm and self.ss == other.ss and self.zz == other.zz:
                ne = False
            return ne
        else:
            raise TypeError
    
    def __lt__( self, other ):
        """This method supports the less than comparison between two Time
        objects."""
        if type( other ) == Time:
            self_hh = self.hh - self.zz
            self_mm = self.mm
            self_ss = self.ss
            other_hh = other.hh - other.zz
            other_mm = other.mm
            other_ss = other.ss
            lt = False
            if self_hh < other_hh:
                lt = True
            elif self_hh == other_hh:
                if self_mm < other_mm:
                    lt = True
                elif self_mm == other_mm:
                    if self_ss < other_ss:
                        lt = True
            return lt
        else:
            raise TypeError
        
    def __le__( self, other ):
        """This method supports the less or equal comparison between two Time
        objects."""
        if type( other ) == Time:
            le = False
            if self.__eq__(other) or self.__lt__(other):
                le = True
            return le
        else:
            raise TypeError
        
    def __gt__( self, other ):
        """This method supports the greater than comparison between two Time
        objects."""
        if type( other ) == Time:
            self_hh = self.hh - self.zz
            self_mm = self.mm
            self_ss = self.ss
            other_hh = other.hh - other.zz
            other_mm = other.mm
            other_ss = other.ss
            gt = False
            if self_hh > other_hh:
                gt = True
            elif self_hh == other_hh:
                if self_mm > other_mm:
                    gt = True
                elif self_mm == other_mm:
                    if self_ss > other_ss:
                        gt = True
            return gt
        else:
            raise TypeError
    
    def __ge__( self, other ):
        """This method supports the greater or equal comparison between two
        Time objects."""
        if type( other ) == Time:
            ge = False
            if self.__eq__(other) or self.__gt__(other):
                ge = True
            return ge
        else:
            raise TypeError
        
    def __add__( self, sec ):
        """This method supports the addition of a Time object and an int object
        (which represents a number of seconds)."""
        if type( sec ) == int:
            self_hh = self.hh
            self_mm = self.mm
            self_ss = self.ss
            other_hh = sec // 3600
            sec = sec % 3600
            other_mm = sec // 60
            sec = sec % 60
            other_ss = sec
            hh = self_hh + other_hh
            mm = self_mm + other_mm
            ss = self_ss + other_ss
            hh -= hh // 24 * 24
            mm -= mm // 60 * 60
            return Time(hh, mm, ss, self.zz)
        else:
            raise TypeError
    
    def __sub__( self, other ):
        """This method supports the subtraction of two Time objects, where the
        result is the number of seconds by which the two times differ."""
        if type( other ) == Time:
            self_hh = self.hh - self.zz
            self_mm = self.mm
            self_ss = self.ss
            other_hh = other.hh - other.zz
            other_mm = other.mm
            other_ss = other.ss
            hh = self_hh - other_hh
            mm = self_mm - other_mm
            ss = self_ss - other_ss
            HOUR_CONVERSION = 3600
            MINUTE_CONVERSION = 60
            sec = HOUR_CONVERSION * hh + MINUTE_CONVERSION * mm + ss
            return sec
        else:
            raise TypeError