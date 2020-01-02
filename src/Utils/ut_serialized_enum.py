# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-2020 Philippe Schmouker, Typee project, http://www.typee.ovh

Permission is hereby granted,  free of charge,  to any person obtaining a copy
of this software and associated documentation files (the "Software"),  to deal
in the Software without restriction, including  without  limitation the rights
to use,  copy,  modify,  merge,  publish,  distribute, sublicense, and/or sell
copies of the Software,  and  to  permit  persons  to  whom  the  Software  is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS",  WITHOUT WARRANTY OF ANY  KIND,  EXPRESS  OR
IMPLIED,  INCLUDING  BUT  NOT  LIMITED  TO  THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT  SHALL  THE
AUTHORS  OR  COPYRIGHT  HOLDERS  BE  LIABLE  FOR  ANY CLAIM,  DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT,  TORT OR OTHERWISE, ARISING FROM,
OUT  OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#=============================================================================
from math    import log2
from struct  import Struct


#=============================================================================
class UTSerializedEnum( Struct ):
    """
    This is a generic meta-class for serialize-able Enum classes.
    CAUTION:
    This is highly pythonized code that intensively takes benefit
    of Python built-in classes and meta-classes goodies.
    """    
    #-------------------------------------------------------------------------
    def __new__(cls, enum_class, bytes_size:int=None):
        '''
        Meta-constructor.
        
        Args:
            enum_class:
                The enumerated class that has to be serialized.
            bytes_size: int
                The number of bytes to store the greatest value of the
                enumerated values. If None, this size is automatically
                deduced from the enumerated values.
                bytes_size has to one one of 1, 2, 4 or 8.
        '''
        if bytes_size is None:
            max_value = max( [e.value for e in enum_class] )
            bits = log2( max_value )
            bytes_count = int( (bits + 7) / 8 )
            bytes_size = [1, 1, 2, 4, 4, 8, 8, 8, 8][bytes_count]
        else:
            assert bytes_size in [1,2,4,8]
        
        super().__init__( ".BH.L...Q"[bytes_size] )
        
        cls._enum_class = enum_class
        cls._dict_encode = { e.value: e for e in enum_class }
        cls._size = bytes_size
        
    #-------------------------------------------------------------------------
    @classmethod
    def read(cls, fp):
        '''
        '''
        value = cls.unpack( fp.read(cls._size) )
        return cls._dict_encode[ value ]
        
    #-------------------------------------------------------------------------
    @classmethod
    def write(cls, fp, value) -> None:
        '''
        '''
        fp.write( cls.pack(value) )

#=====   end of   Utils.ut_serialized_enum   =====#
        