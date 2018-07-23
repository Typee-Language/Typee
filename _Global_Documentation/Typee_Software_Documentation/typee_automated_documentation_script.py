#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2018 Philippe Schmouker, Typee project, http://www.typee.ovh

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
from os import rename as os_rename, remove as os_remove
from PyYadc.src.html_generator import HtmlGenerator


#=============================================================================
if __name__ == '__main__':
    """
    This script runs PyYadc onto directory 'src/' of this Typee software.
    """

    print( "Generating documentation for Typee Project" )
    HtmlGenerator( '../../../Typee/src', "Typee Software Documentation" )
    
    
    src_docpath = '../../src/src_doc.html'
    dst_docpath = 'typee_software_doc.html'
    
    try:
        os_rename( src_docpath, dst_docpath )
    except OSError:
        os_remove( dst_docpath )
        os_rename( src_docpath, dst_docpath )
            
    
    print( '-- done!' )

#=====   end of   _Global_Documentation.Typee_Software_Documentation.typee_automated_documentation_script   =====#
