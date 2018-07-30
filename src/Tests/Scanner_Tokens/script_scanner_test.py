#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 Philippe Schmouker, Typhon project, http://www.typee.ovh

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
from test_compound_tokens        import test_compound_tokens
from test_names_and_nums_tokens  import test_names_and_nums_tokens
from test_simple_tokens          import test_simple_tokens

#=============================================================================
if __name__ == '__main__':
    """
    This script calls every test functions dedicated to the Front-End Scanner.
    """
    #-------------------------------------------------------------------------
    test_compound_tokens()
    test_names_and_nums_tokens()
    test_simple_tokens()
   

#=====   end of   Tests.Scanner_Tokens.script_scanner_test   =====#
