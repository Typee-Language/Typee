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
from importlib import import_module

from FrontEnd.IntermediateCode.fe_icode_tokens   import FEICodeTokens
from FrontEnd.Scanner.fe_scanner                 import FEScanner


#=============================================================================
class TokensTestBase:
    """
    Base class for all tokens tests.
    """    
    #-------------------------------------------------------------------------
    def __init__(self, test_title:str, test_src_path:str, soluce_path:str):
        '''
        Constructor.
        Automatically runs the test.
        
        
        Args:
            test_title: str
                The title (i.e. name) of this test
            test_src_path: str
                the path to the Typee test file
            soluce_path: str
                the path to the file that contains the  expected  list  of
                Intermediate Code nodes. This list HAS TO BE NAMED soluce.
        
        Raises:
            IOError: some file has not been found or can't be opened.
        '''
        print( "--", test_title )
        
        scanner = FEScanner()
        icode = scanner.scan_file( test_src_path )
        
        if soluce_path.endswith( '.py' ):
            soluce_path = soluce_path[:-3]

        solution = import_module( soluce_path.replace('/','.') )
        
        self.err_count = 0
        for i, (s, c) in enumerate( zip(solution.soluce, icode) ):
            if not s == c:
                print( ' line {:d}:{:d} - node {:d} -- coded {:s}({}) != expected {:s}({})'.format(
                    c.num_line, c.num_coln, i, 
                    FEICodeTokens.token_name( c.tk_ident ),
                    c.tk_data,
                    FEICodeTokens.token_name( s.tk_ident ),
                    s.tk_data
                  ) )
                self.err_count+= 1
        
        if self.err_count == 0:
            print( '   Ok!' )
        else:
            print( '   {:d} error{:s}'.format(self.err_count, 's' if self.err_count > 1 else '') )

    #-------------------------------------------------------------------------
    def is_ok(self) -> bool:
        return self.err_count == 0

#=====   end of   Tests.tokens_test_base   =====#
        
