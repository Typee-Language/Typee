# -*- coding: utf-8 -*-

"""
Copyright (c) 2018-2019 Philippe Schmouker, Typhee project, http://www.typee.ovh

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
from FrontEnd.IntermediateCode.fe_icode_token_node import *


#=============================================================================
soluce = [
    
    ICTokenNode_COMMENT( None, " Simple tokens -- tokenization test source" ),
    ICTokenNode_NL(),
    ICTokenNode_BRACKETOP(),
    ICTokenNode_BRACKETCL(),
    ICTokenNode_NL(),
    ICTokenNode_PAROP(),
    ICTokenNode_PARCL(),
    ICTokenNode_NL(),
    ICTokenNode_COMMA(),
    ICTokenNode_SEMICOLON(),
    ICTokenNode_NL(),
    ICTokenNode_HASH(),
    ICTokenNode_NL(),
    ICTokenNode_DOT(),
    ICTokenNode_NL(),
    ICTokenNode_TILD(),
    ICTokenNode_NL(),
    ICTokenNode_ANY_TYPE( None, '?' ),
    ICTokenNode_NL(),
    ICTokenNode_EOF()
]

#=====   end of   Tests.Data.tokenization_simple_solution   =====#
        