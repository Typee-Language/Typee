#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2018 Philippe Schmouker, Typhee project, http://www.typee.ovh

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
from FrontEnd.IntermediateCode.fe_icode_node import *


#=============================================================================
soluce = [
    
    ICNode_COMMENT( None, " Simple tokens -- tokenization test source" ),
    ICNode_NL(),
    ICNode_BRACKETOP(),
    ICNode_BRACKETCL(),
    ICNode_NL(),
    ICNode_PAROP(),
    ICNode_PARCL(),
    ICNode_NL(),
    ICNode_COMMA(),
    ICNode_SEMICOLON(),
    ICNode_NL(),
    ICNode_HASH(),
    ICNode_NL(),
    ICNode_DOT(),
    ICNode_NL(),
    ICNode_TILD(),
    ICNode_NL(),
    ICNode_ANY_TYPE( None, '?' ),
    ICNode_NL(),
    ICNode_EOF()
]

#=====   end of   Tests.Data.tokenization_simple_solution   =====#
        