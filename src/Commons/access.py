# -*- coding: utf-8 -*-
"""
Copyright (c) 2018-2019 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from enum import IntEnum, auto

from Utils.ut_serialized_enum import UTSerializedEnum


#=============================================================================
class Access( IntEnum ):
    """
    Descriptors for access roles on variables, functions, classes and methods.
    This class is just used as a namespace.
    """
    #--------------------------------------------------------------------------
    PUBLIC    = auto()
    PROTECTED = auto()
    HIDDEN    = auto()


#=============================================================================
class AccessStack( list ):
    """
    The class of push-and-pop stacks containing access qualifiers.
    To be used for the storage of  current access status along the
    nested instructions blocks (i.e. levels of braces).
    """
    #--------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self._current_level = 0
        self.append( self._DEFAULT )

    #-------------------------------------------------------------------------
    def add_level(self, access_qualif:Access=None):
        self._current_level += 1
        try:
            self[ self._current_level ] = access_qualif or self._DEFAULT
        except:
            self.append( access_qualif or self._DEFAULT )
    
    #-------------------------------------------------------------------------
    def get_current(self) -> Access:
        return self[ self._current_level ]
    
    #-------------------------------------------------------------------------
    def suppress_level(self):
        if self._current_level > 0:
            self._current_level -= 1

    #--------------------------------------------------------------------------
    # Class data
    _DEFAULT = Access.PUBLIC


#=============================================================================
class SerializedAccess( UTSerializedEnum ):
    """
    This class eases the serialization of protection access values in files.
    It offers read() and write() goodies of Access values from and to files.
    """
    #-------------------------------------------------------------------------
    def __new__(cls):
        '''
        Class meta-constructor.
        '''
        super().__new__( Access )

#=====   end of   Commons.access   =====#
