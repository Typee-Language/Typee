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
soluce = [ ICNode_COMMENT( None, " Compound tokens -- tokenization test source" ),
           ICNode_NL(),
           ICNode_COMMENT_ML( None, "**\nmulti-lines comment\n**" ),
           ICNode_NL(),
           ICNode_AROBASE(),
           ICNode_AUG_AROBASE(),
           ICNode_NL(),
           ICNode_BITAND(),
           ICNode_AUG_BITAND(),
           ICNode_NL(),
           ICNode_BITOR(),
           ICNode_AUG_BITOR(),
           ICNode_NL(),
           ICNode_BITXOR(),
           ICNode_POWER( None, '^^'),
           ICNode_AUG_BITXOR(),
           ICNode_AUG_POWER( None, '^^='),
           ICNode_NL(),
           ICNode_COLON(),
           ICNode_OP_2COLN(),
           ICNode_AUG_2COLN(),
           ICNode_NL(),
           ICNode_DIV(),
           ICNode_AUG_DIV(),
           ICNode_NL(),
           ICNode_ASSIGN(),
           ICNode_EQ(),
           ICNode_NL(),
           ICNode_UNEXPECTED(None, ' '),
           ICNode_OP_2EXCL(),
           ICNode_NE(),
           ICNode_AUG_2EXCL(),
           ICNode_NL(),
           ICNode_ANY_TYPE(),
           ICNode_OP_2QUEST(),
           ICNode_ANY_TYPE(),
           ICNode_ASSIGN(),
           ICNode_AUG_2QUEST(),
           ICNode_NL(),
           ICNode_GT(),
           ICNode_SHIFTR(),
           ICNode_SHIFT0R(),
           ICNode_GE(),
           ICNode_AUG_SHIFTR(),
           ICNode_AUG_SHIFT0R(),
           ICNode_OP_GRLE(),
           ICNode_AUG_GRLE(),
           ICNode_NL(),
           ICNode_LT(),
           ICNode_SHIFTL(),
           ICNode_SHIFT0L(),
           ICNode_LE(),
           ICNode_AUG_SHIFTL(),
           ICNode_AUG_SHIFT0L(),
           ICNode_NL(),
           ICNode_MINUS(),
           ICNode_DECR(),
           ICNode_AUG_MINUS(),
           ICNode_ISOF(),
           ICNode_NL(),
           ICNode_MOD(),
           ICNode_AUG_MOD(),
           ICNode_NL(),
           ICNode_PLUS(),
           ICNode_INCR(),
           ICNode_AUG_PLUS(),
           ICNode_NL(),
           ICNode_MUL(),
           ICNode_POWER( None, '**' ),
           ICNode_AUG_MUL(),
           ICNode_AUG_POWER( None, '**=' ),
           ICNode_NL(),
           ICNode_COLON(),
           ICNode_ASSIGN(),
           ICNode_DECR(),
           ICNode_ASSIGN(),
           ICNode_INCR(),
           ICNode_ASSIGN(),
           ICNode_LT(),
           ICNode_MINUS(),
           ICNode_NL(),
           ICNode_DOT(),
           ICNode_ELLIPSIS(),
           ICNode_UNEXPECTED(None, 'a'),
           ICNode_NL(),
           ICNode_COMMENT(None, "/* */"),
           ICNode_NL(),
           ICNode_BRACEOP(),
           ICNode_BRACECL(),
           ICNode_EMBED_CODE(None, " " ),
           ICNode_NL(), 
           ICNode_EOF()
          ]

#=====   end of   Tests.Data.tokenization_simple_solution   =====#
        