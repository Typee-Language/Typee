#!/usr/bin/env python
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
from local_tools.copyright_years_modif import CopyrightYearsModif

#=============================================================================
if __name__ == '__main__':
    """
    Runs the script function.
    """
    #-------------------------------------------------------------------------
    my_copyright_modifier = CopyrightYearsModif()
    
    my_copyright_modifier.modify_directories( ['../BackEnd',
                                               '../Commons',
                                               '../FrontEnd',
                                               '../local_tools',
                                               '../Tests',
                                               '../Utils',
                                               '../../Language-specifications'] )
    
    my_copyright_modifier.modify_files( ['../../development-framework.md',
                                         '../../LICENSE',
                                         '../../notepad-readme.md',
                                         '../../README.md'] )

#=====   end of   local_tools.script_copyright_automated_modification   =====#