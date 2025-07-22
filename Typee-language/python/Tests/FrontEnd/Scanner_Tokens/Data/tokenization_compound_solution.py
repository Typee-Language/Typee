# -*- coding: utf-8 -*-

"""
Copyright (c) 2018-2021 Philippe Schmouker, Typhee project, http://www.typee.ovh

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
soluce = [ ICTokenNode_COMMENT( None, " Compound tokens -- tokenization test source" ),
           ICTokenNode_NL(),
           ICTokenNode_COMMENT_ML( None, "**\nmulti-lines comment\n**" ),
           ICTokenNode_NL(),
           ICTokenNode_AROBASE(),
           ICTokenNode_AUG_AROBASE(),
           ICTokenNode_OP_2AROB(),
           ICTokenNode_AUG_2AROB(),
           ICTokenNode_NL(),
           ICTokenNode_BITAND(),
           ICTokenNode_AUG_BITAND(),
           ICTokenNode_NL(),
           ICTokenNode_BITOR(),
           ICTokenNode_AUG_BITOR(),
           ICTokenNode_NL(),
           ICTokenNode_BITXOR(),
           ICTokenNode_POWER( None, '^^'),
           ICTokenNode_AUG_BITXOR(),
           ICTokenNode_AUG_POWER( None, '^^='),
           ICTokenNode_NL(),
           ICTokenNode_COLON(),
           ICTokenNode_AUG_COLN(),
           ICTokenNode_OP_2COLN(),
           ICTokenNode_AUG_2COLN(),
           ICTokenNode_NL(),
           ICTokenNode_DIV(),
           ICTokenNode_AUG_DIV(),
           ICTokenNode_NL(),
           ICTokenNode_ASSIGN(),
           ICTokenNode_EQ(),
           ICTokenNode_NL(),
           ICTokenNode_EXCL(),
           ICTokenNode_OP_2EXCL(),
           ICTokenNode_NE(),
           ICTokenNode_AUG_2EXCL(),
           ICTokenNode_NL(),
           ICTokenNode_ANY_TYPE(),
           ICTokenNode_OP_2QUEST(),
           ICTokenNode_ANY_TYPE(),
           ICTokenNode_ASSIGN(),
           ICTokenNode_AUG_2QUEST(),
           ICTokenNode_NL(),
           ICTokenNode_GT(),
           ICTokenNode_SHIFTR(),
           ICTokenNode_SHIFT0R(),
           ICTokenNode_GE(),
           ICTokenNode_AUG_SHIFTR(),
           ICTokenNode_AUG_SHIFT0R(),
           ICTokenNode_OP_GRLE(),
           ICTokenNode_AUG_GRLE(),
           ICTokenNode_NL(),
           ICTokenNode_LT(),
           ICTokenNode_SHIFTL(),
           ICTokenNode_SHIFT0L(),
           ICTokenNode_LE(),
           ICTokenNode_AUG_SHIFTL(),
           ICTokenNode_AUG_SHIFT0L(),
           ICTokenNode_LEG(),
           ICTokenNode_OP_LEGR(),
           ICTokenNode_AUG_LEGR(),
           ICTokenNode_NL(),
           ICTokenNode_MINUS(),
           ICTokenNode_DECR(),
           ICTokenNode_AUG_MINUS(),
           ICTokenNode_ISOF(),
           ICTokenNode_NL(),
           ICTokenNode_MOD(),
           ICTokenNode_AUG_MOD(),
           ICTokenNode_NL(),
           ICTokenNode_PLUS(),
           ICTokenNode_INCR(),
           ICTokenNode_AUG_PLUS(),
           ICTokenNode_NL(),
           ICTokenNode_MUL(),
           ICTokenNode_POWER( None, '**' ),
           ICTokenNode_AUG_MUL(),
           ICTokenNode_AUG_POWER( None, '**=' ),
           ICTokenNode_NL(),
           ICTokenNode_DECR(),
           ICTokenNode_ASSIGN(),
           ICTokenNode_INCR(),
           ICTokenNode_ASSIGN(),
           ICTokenNode_LT(),
           ICTokenNode_MINUS(),
           ICTokenNode_NL(),
           ICTokenNode_DOT(),
           ICTokenNode_ELLIPSIS(),
           ICTokenNode_UNEXPECTED(None, 'a'),
           ICTokenNode_NL(),
           ICTokenNode_COMMENT(None, "/* */"),
           ICTokenNode_NL(),
           ICTokenNode_BRACEOP(),
           ICTokenNode_BRACECL(),
           ICTokenNode_EMBED_CODE(None, " " ),
           ICTokenNode_NL(), 
           ICTokenNode_EOF()
          ]

#=====   end of   Tests.Data.tokenization_simple_solution   =====#
        